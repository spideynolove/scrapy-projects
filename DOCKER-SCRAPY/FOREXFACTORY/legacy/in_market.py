from scrapy import Spider, Request
from crawldata.functions import *
from requests import get, post
from scrapy.http import HtmlResponse
from json import loads
from urllib.parse import urlencode


class CrawlerSpider(Spider):
    name = "Market"
    check_dirs(f"{PROJECT_PATH}/_log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
    }

    headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
    params = {'more': '1', }

    def start_requests(self):
        # for symbol in SYMBOLS:
        for symbol in ('GBPUSD',):
            symbol = symbol.lower()
            # Latest news
            data = f'-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentNews_instrumentNews][idSuffix]"\r\n\r\n{symbol}\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentNews_instrumentNews][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentNews_instrumentNews][modelData]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096--\r\n'
            response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
            yield Request('https://www.google.com', meta={'data': (response.text, symbol)}, dont_filter=True)

    def parse(self, response):
        data, symbol = response.meta['data']
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        results = {'latest': dict()}
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['latest'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Hottest stories
        data = f'-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentHottestNews_instrumentHottestNews][idSuffix]"\r\n\r\n{symbol}\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentHottestNews_instrumentHottestNews][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[InstrumentHottestNews_instrumentHottestNews][modelData]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': (response.text, results, symbol)}, dont_filter=True, callback=self.parse_hottest)

    def parse_hottest(self, response):
        data, results, symbol = response.meta['data']
        results['hottest'] = dict()
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['hottest'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Upcoming
        up_params = {'limit': '55', }
        symbol = symbol.upper()
        url = f'https://www.forexfactory.com/upcoming/{symbol}?' + urlencode(up_params)
        response = get(url, headers=headers)
        yield Request('https://www.google.com', meta={'data': (response.text, results, symbol)}, dont_filter=True, callback=self.parse_upcoming)

    def parse_upcoming(self, response):
        updata, results, symbol = response.meta['data']
        data = loads(updata)
        results['upcoming'] = dict()
        for item in data.get('events'):
            id_ = item.get('id')
            results['upcoming'].setdefault(id_, {
                'title ': item.get('title'),
                'impact': item.get('impact_name'),
                'day ': get_unixtime(item.get('dateline'), divide=1),
                'forecast ': get_num(item.get('forecast')),
                'previous ': get_num(item.get('previous')),
            })

        # Bars data
        symbol = symbol[:3] + '/' + symbol[3:]
        bar_params = {
            # full monthly history
            'to': '1682974800',     # change this for specific time range
            'per_page': '9999',

            'interval': 'MN1',  # change this for OHLC data
            'instrument': symbol,
            'extra_fields': '',
        }
        url = f'https://mds-api.forexfactory.com/bars?' + urlencode(bar_params)
        response = get(url, headers=headers)
        yield Request('https://www.google.com', meta={'data': (response.text, results, symbol)}, dont_filter=True, callback=self.parse_bars)

    def parse_bars(self, response):
        barsdata, results, symbol = response.meta['data']
        results['bars'] = dict()
        data = loads(barsdata)
        for item in data.get('data'):
            instrument = item.get('instrument')
            time_ = get_unixtime(item.get('timestamp'), divide=1)
            results['bars'].setdefault(time_, {
                'open': item.get('open'),
                'high': item.get('high'),
                'low': item.get('low'),
                'close': item.get('close'),
                'interval': item.get('interval'),
            })

        # performace: (bar numbers + timeframe) list
        response = get('https://mds-api.forexfactory.com/bars/aggregate?requests[]=GBP%2FUSD,12,H4', headers=headers)



    def parse_performace(self, response):
        pass

# Positions

# instrument

# macro
