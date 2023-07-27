from scrapy import Spider, Request
from crawldata.functions import *
from requests import get
from json import loads
from urllib.parse import urlencode


class CrawlerSpider(Spider):
    name = "Bars"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        to_d = get_unix(NOW, 1)
        for symbol in TEST_SYMBOLS:
            symbol_ = symbol[:3] + '/' + symbol[3:]
            for interval in INTERVALS:
                bar_params = {
                    'to': to_d,
                    'per_page': '9999',
                    'interval': interval,
                    'instrument': symbol_,
                    'extra_fields': '',
                }
                url = f'https://mds-api.forexfactory.com/bars?' + urlencode(bar_params)
                response = get(url, headers=headers)
                yield Request('https://www.google.com', meta={'data': (response.text, interval, symbol)}, dont_filter=True)

    def parse(self, response):
        data, interval, symbol = response.meta['data']
        data = loads(data)
        rnum = 2 if any(ext in symbol for ext in QUOTECHECK) else 4

        results = dict()
        for item in data.get('data'):
            time_ = get_unixtime(item.get('timestamp'), divide=1)
            results.setdefault(time_, {
                'open': get_number(item.get('open'), rnum),
                'high': get_number(item.get('high'), rnum),
                'low': get_number(item.get('low'), rnum),
                'close': get_number(item.get('close'), rnum),
            })

        yield {f"{symbol}-{interval}": results,}