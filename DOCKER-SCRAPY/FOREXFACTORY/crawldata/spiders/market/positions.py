# from scrapy import Spider, Request
# from scrapy.selector import Selector
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_positions"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }

#     def __init__(self, *args, **kwargs): 
#         super(CrawlerSpider, self).__init__(*args, **kwargs) 
#         self.endpoints = kwargs.get('params').split(',')

#     def start_requests(self):
#         symbol, limit, interval = self.endpoints
#         params = {
#             'onlyContent': 'true',
#             'section': 'details',
#             'currency': symbol.upper(),
#             'row': '0',
#         }
#         headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
#         data = f'-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nyes\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][idSuffix]"\r\n\r\n{symbol}\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][modelData]"\r\n\r\neyJzaW5nbGVfaW5zdHJ1bWVudCI6IlVTRENIRiIsIl9fZmxleERlZmF1bHRzX18iOnsidHJhZGVzXC9wb3NpdGlvbnNcL3R5cGUiOiJkdWFsIn19\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][trades/positions/type]"\r\n\r\ndual\r\n-----------------------------48222048032047603611657549096--\r\n'
#         response = post('https://www.forexfactory.com/flex.php', params=params, headers=headers, data=data)
#         yield Request('https://www.google.com', meta={'data': (response.text, symbol, limit, interval)}, dont_filter=True)

#     def parse(self, response):
#         data, symbol, limit, interval = response.meta['data']
#         stats = dict()
#         for item in Selector(text=data).xpath("(//table)[1]/tbody/tr"):
#             values = clean_lst(item.xpath("./descendant::*/text()").getall())
#             stats.setdefault(values[0], values[1:])

#         params = {
#             'content': 'positions',
#             'do': 'positions_graph_data',
#             'currency': symbol.upper(),
#             'interval': interval,
#             'limit': limit,
#         }
#         url = 'https://www.forexfactory.com/explorerapi.php?' + urlencode(params)
#         response = get(url, headers=headers)
#         yield Request('https://www.google.com', dont_filter=True,  callback=self.parse_ratio,
#                         meta={'data': (response.text, symbol, stats, interval)},)

#     def parse_ratio(self, response):
#         data, symbol, stats, interval = response.meta['data']
#         data = loads(data)
#         keys = ('currency_code', 'timeframe', 'id', 'weekend', 'traders_is_low', 'pos', 'datetime', 'hidden')
#         positions = dict()
#         for item in data.get('positions'):
#             time_ = item.pop('dateline')
#             if time_ > int(get_unix(NOW, 1)): 
#                 break
#             time_ = get_unixtime(time_, divide=1, have_hour=True)
#             item = {key: round(item[key], 4) for key in item if key not in keys}
#             positions.setdefault(time_, item)
#         yield {f"{symbol}_{interval}_positions": {'stats': stats, 'positions': positions}}