from scrapy import Spider, Request
from crawldata.functions import *
from requests import get
from json import loads


class CrawlerSpider(Spider):
    name = "Performances"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 2,
    }

    def start_requests(self):
        for item in gen_perform(TEST_SYMBOLS, CHG_PERIODS):
            url = f'https://mds-api.forexfactory.com/bars/aggregate?requests[]={item}'
            response = get(url, headers=headers)
            yield Request('https://www.google.com', meta={'data': (response.text, *revert_perform(item))}, dont_filter=True)

    def parse(self, response):
        data, symbol, period = response.meta['data']
        data = loads(data)
        rnum = 2 if any(ext in symbol for ext in QUOTECHECK) else 4
        
        results = dict()
        for _, values in data.items():
            for item in values.get('data'):
                time_ = get_unixtime(item.get('timestamp'), divide=1)
                results.setdefault(time_, {
                    'open': get_number(item.get('open'), rnum),
                    'high': get_number(item.get('high'), rnum),
                    'low': get_number(item.get('low'), rnum),
                    'close': get_number(item.get('close'), rnum),
                })
        yield {f"{symbol}-{period}": results,}