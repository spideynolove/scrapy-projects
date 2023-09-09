from scrapy import Spider, Request
from crawldata.functions import *
from urllib.parse import urlencode
from json import loads
from requests import get
from scrapy.http import HtmlResponse


class CrawlerSpider(Spider):
    name = "PositionRatio"
    check_dirs(f"{PROJECT_PATH}/_log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        # 'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        params = {
            'content': 'positions',
            'do': 'positions_graph_data',
            'currency': 'EURUSD',
            'interval': 'D1',
            'limit': '200',
        }
        url = 'https://www.forexfactory.com/explorerapi.php?' + \
            urlencode(params)
        response = get(url, headers=headers)
        yield Request('https://www.google.com', meta={'data': response.text}, dont_filter=True)

    def parse(self, response):
        data = loads(response.meta['data'])
        # response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        print(data.get('total'))
        # print(data.get('positions'))
        print(data.get('data_count'))
        print(data.get('has_more'))
        print(data.get('interval'))
        print(data.get('currency'))
        print(data.get('limit'))
        
        # data = response.meta['data']
        # response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        # jdata = loads(response.text)
        # # print(jdata.get('meta'))

        # for item in jdata.get('data').get('events')[:10]:
        #     date_ = get_time(item.get('date'), have_hour=False)
        #     actual = get_num(item.get('actual'))
        #     forecast = get_num(item.get('forecast'))
        #     print(date_, actual, forecast)
