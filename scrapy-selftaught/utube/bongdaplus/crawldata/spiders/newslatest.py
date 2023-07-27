from scrapy import Spider, Request, FormRequest
from crawldata.functions import *


class CrawlerSpider(Spider):
    name = "Newslatest"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }

    def start_requests(self):
        yield Request('https://bongdaplus.vn/newslatest/0', headers=headers, meta={'page': 0})
        
    def parse(self, response):
        # page = response.meta['page']
        for item in response.xpath("//li[@class='news']/a"):
            url = response.urljoin(item.xpath("./@href").get())
            id_ = url.split('-')[-1][:-9]
            if id_ != '402763':
                continue
            if not any(term in url for term in FORBIDDEN):
                comdata['objectid'] = id_
                comdata['comment'] = 'Trong cái rủi có cái may, bị 7 chọ đá ghế lại có chỗ làm tốt hơn, kaka'
                yield FormRequest('https://bongdaplus.vn/postcomment/', headers=headers, formdata=comdata)
        # if page < 9:
        #     page += 1
        #     yield Request(f'https://bongdaplus.vn/newslatest/{page}', headers=headers, meta={'page': page})