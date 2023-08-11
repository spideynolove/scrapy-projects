import sys
from crawldata.functions import *
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings as settings

def create_client(name: str = None, urls: object = None):
    redisClient = from_url(settings().get('REDIS_URL'))   
    for url in urls:
        # print(url)
        redisClient.lpush(name, url)

def start_spider(spider, settings: dict = {}, data: dict = {}):
    use_bloom, job = data.get('use_bloom'), data.get('job')
    all_settings = {**settings, **{'SELF_CONFIG': data, 'ITEM_PIPELINES': 
                                   {'crawldata.pipelines.CrawldataPipeline': 300,}}}
    def crawler_func():
        crawler_process = CrawlerProcess(all_settings)
        crawler_process.crawl(spider, page=job) if use_bloom else crawler_process.crawl(spider)
        crawler_process.start()
    process = Process(target=crawler_func)
    process.start()
    return process

if __name__ == '__main__':
    with open(f'{MIC_PATH}/clubs.json') as data:
        parsed_json = load(data)
    ids = [item.get('team').get('id') for item in parsed_json]
    name, jobs, page_num = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    data = dict()
    if 'bloom' in name:
        data = {
            'use_bloom': True,
            'SCHEDULER': "scrapy_redis_bloomfilter.scheduler.Scheduler",
            'DUPEFILTER_CLASS': "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter",
            'SCHEDULER_PERSIST': True,
            'BLOOMFILTER_HASH_NUMBER': 6,
            'BLOOMFILTER_BIT': 10,
        }
    else:
        data = {
            'use_bloom': False,
            'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
            'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
            'SCHEDULER_PERSIST': True,
            'SCHEDULER_QUEUE_CLASS': 'scrapy_redis.queue.SpiderQueue',
        }
        # bases = [fill_quote(base, page, id_) for page in range(page_num) for id_ in ids]
        urls = list()
        for page in range(page_num):
            for id_ in ids:
                fixparams['page'] = page
                fixparams['teams'] = id_
                urls.append(gen_urls(params=fixparams))
        create_client(f"{name}:start_urls", urls)
    map(lambda x: x.join(),[start_spider(name, settings=settings(), data={**data, 'job': i+1,}) for i in range(jobs)])