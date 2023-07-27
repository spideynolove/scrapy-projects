from scrapy import Spider, Request
from crawldata.functions import *
from urllib.parse import urlencode
from json import loads
from requests import post, get
from scrapy.http import HtmlResponse


class CrawlerSpider(Spider):
    name = "Positions"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 2,
    }

    def start_requests(self):
        headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
        for symbol in TEST_SYMBOLS:
            symbol_ = symbol.lower()
            params = {
                'onlyContent': 'true',
                'section': 'details',
                'currency': symbol,
                'row': '0',
            }
            data = f'-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nyes\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][idSuffix]"\r\n\r\n{symbol_}\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][modelData]"\r\n\r\neyJzaW5nbGVfaW5zdHJ1bWVudCI6IlVTRENIRiIsIl9fZmxleERlZmF1bHRzX18iOnsidHJhZGVzXC9wb3NpdGlvbnNcL3R5cGUiOiJkdWFsIn19\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][trades/positions/type]"\r\n\r\ndual\r\n-----------------------------48222048032047603611657549096--\r\n'
            response = post('https://www.forexfactory.com/flex.php', params=params, headers=headers, data=data)
            yield Request('https://www.google.com', meta={'data': (response.text, symbol)}, dont_filter=True)

    def parse(self, response):
        data, symbol = response.meta['data']
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        columns = clean_lst(response.xpath("(//table)[1]/thead/descendant::*/text()").getall())
        results = dict()
        results.setdefault(symbol, dict())
        results[symbol].setdefault('stats', dict())

        for item in response.xpath("(//table)[1]/tbody/tr"):
            values = clean_lst(item.xpath("./descendant::*/text()").getall())
            results[symbol]['stats'].setdefault(values[0], dict(zip(columns, values[1:])))

        # Ratio
        results[symbol].setdefault('BB_ratio', dict())
        # for tf in ('D1',):
        for tf in BB_PERIODS:
            ratioparams = {
                'content': 'positions',
                'do': 'positions_graph_data',
                'currency': symbol,
                'interval': tf,
                'limit': '800',
                # 'limit': '400',
            }
            url = 'https://www.forexfactory.com/explorerapi.php?' + urlencode(ratioparams)
            response = get(url, headers=headers)
            yield Request('https://www.google.com', dont_filter=True, 
                          callback=self.parse_ratio,
                          meta={'data': (response.text, symbol, results, tf)},)

    def parse_ratio(self, response):
        current = get_unix(NOW, 1)
        data, symbol, results, tf = response.meta['data']
        data = loads(data)

        results[symbol]['BB_ratio'].setdefault(tf, dict())
        for item in data.get('positions'):
            if item.get('dateline') > int(current): 
                break
            
            # get first time then just update in the next get
            time_ = get_unixtime(item.get('dateline'), divide=1)
            results[symbol]['BB_ratio'][tf].setdefault(time_, {
                'id': item.get('id'),
                'short_lots': get_number(item.get('short_lots'), 2),
                'long_lots': get_number(item.get('long_lots'), 2),
                'traders_short': get_num(item.get('traders_short')),
                'traders_long': get_num(item.get('traders_long')),
                'lots_ratio': get_number(item.get('lots_ratio'), 2),
                'traders_ratio': get_number(item.get('traders_ratio'), 2),
                'dummy_lots': get_number(item.get('dummy_lots'), 2),
                'dummy_traders': get_number(item.get('dummy_traders'), 2),
            })
        if len(results[symbol]['BB_ratio']) == len(BB_PERIODS):
            yield results
        