from scrapy import Spider, Request
from crawldata.functions import *
from urllib.parse import urlencode
from json import loads
from requests import post, get
from scrapy.http import HtmlResponse


class CrawlerSpider(Spider):
    name = "Upcoming"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        # 'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        for symbol in TEST_SYMBOLS:
            url = f'https://www.forexfactory.com/upcoming/{symbol}?' + urlencode({'limit': '55', })
            response = get(url, headers=headers)
            yield Request('https://www.google.com', meta={'data': (response.text, symbol)}, dont_filter=True)

    def parse(self, response):
        data, symbol = response.meta['data']
        data = loads(data)
        results = dict()
        results.setdefault(symbol, dict())
        for item in data.get('events'):
            id_ = item.get('id')
            results[symbol].setdefault(id_, {
                'title ': item.get('title'),
                'impact': item.get('impact_name'),
                'day ': get_unixtime(item.get('dateline'), divide=1),
                'forecast ': get_num(item.get('forecast')),
                'previous ': get_num(item.get('previous')),
            })

        time_ = get_unix(NOW, 1)
        # Indicator news: M1, M5, H1, H4, D1, MN1
        event_params = {
            'instrument': 'GBP/USD',
            'interval': 'D1',
            'from': '1661374800',
            'to': time_,
        }
        url = f'https://mds-api.forexfactory.com/indicators/news?' + urlencode(event_params)
        response = get(url, headers=headers)
        yield Request('https://www.google.com', dont_filter=True,
                      meta={'data': (response.text, symbol)}, callback=self.parse_news)
    
    def parse_news(self, response):
        pass