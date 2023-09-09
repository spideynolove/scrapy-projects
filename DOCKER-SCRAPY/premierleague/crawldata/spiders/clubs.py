from scrapy import Request, Spider
from crawldata.functions import *
from crawldata.items import ClubItem


class CrawlerSpider(Spider):
    name = "seasons"
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }
    base = 'https://footballapi.pulselive.com/football/standings?{}'

    def __init__(self, *args, **kwargs): 
        super(CrawlerSpider, self).__init__(*args, **kwargs) 
        tblparams['compSeasons'] = int(kwargs.get('season'))  # 489 ~ 2022/23

    def start_requests(self):
        open(f'{MIC_PATH}/{self.name}.json', 'w').close()
        yield Request(self.base.format(urlencode(tblparams)))

    def parse(self, response):
        data = loads(response.text)
        for item in data.get('tables')[0].get('entries'):
            yield ClubItem({
                'team': item.get('team').get('club'),
                'ground': item.get('ground'),
            })