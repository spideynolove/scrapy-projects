from scrapy import Spider, Request
from crawldata.functions import *
from json import loads


class CrawlerSpider(Spider):
    name = "InstrumentPrices"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        # 'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        prefix = ("requests[]=", )
        SYMBOLS = [
            'EUR/USD', 'GBP/USD', 'AUD/USD', 'NZD/USD',
            'USD/JPY', 'USD/CHF', 'USD/CAD',
            'GBP/JPY', 'GBP/AUD', 'GBP/NZD', 'GBP/CAD', 'GBP/CHF',
            'EUR/JPY', 'EUR/AUD', 'EUR/NZD', 'EUR/CAD', 'EUR/CHF',
            'EUR/GBP',
        ]
        # can config in external param
        subfix = (",12,M30", ",24,H1", ",12,H4")
        outcome = list()
        for symbol in SYMBOLS:
            symbol = symbol.replace('/', '%2F')
            string = [f"{a}{b}" for a, b in zip([symbol,]*len(subfix), subfix)]
            string = [f"{a}{b}" for a, b in zip(prefix*len(subfix), string)]
            outcome.append(string)
        outcome = 'https://mds-api.forexfactory.com/bars/aggregate?' + \
            '&'.join(flatten(outcome))
        yield Request(outcome, headers=headers)

    def parse(self, response):
        totaldata = loads(response.text)
        quotes = dict()
        for item, data in totaldata.items():
            symbol, periods, timeframe = item.split(',')
            symbol = symbol.replace('/', '')
            historical = dict()
            for minor in data.get('data'):
                time_ = get_unixtime(minor.get('timestamp'), divide=1)
                historical.setdefault(time_, {
                    'open': get_num(minor.get('open')),
                    'high': get_num(minor.get('high')),
                    'low': get_num(minor.get('low')),
                    'close': get_num(minor.get('close')),
                })
            quotes.setdefault(f'{symbol}_{timeframe}', {
                'historical': historical,
                'periods': periods
            })
        yield quotes
