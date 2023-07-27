from scrapy import Spider, Request
from crawldata.functions import *
from urllib.parse import urlencode
from json import loads


class CrawlerSpider(Spider):
    '''get all instrumens and macros'''
    name = "Instruments"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        # 'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        # SYMS = MACROSYMBOLS if self.group == 'macro' else SYMBOLS
        SYMS = MACROSYMBOLS + SYMBOLS
        symbols = [f'{item[:-3]}/{item[-3:]}' for item in SYMS]
        params = {'instruments': ','.join(symbols), }
        url = f"https://mds-api.forexfactory.com/instruments?{urlencode(params)}"
        yield Request(url, headers=headers)

    def parse(self, response):
        data = loads(response.text)
        for item in data.get('data'):
            instrument = item.get('instrument').get('name').replace('/', '')
            yield {instrument: item.get('metrics')}