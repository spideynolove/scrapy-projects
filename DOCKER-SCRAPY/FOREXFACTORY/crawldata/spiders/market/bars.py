# from scrapy import Spider, Request
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_bars"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }

#     def __init__(self, *args, **kwargs): 
#         super(CrawlerSpider, self).__init__(*args, **kwargs) 
#         self.endpoints = kwargs.get('params').split(',')

#     def start_requests(self):
#         symbol, number, interval = self.endpoints
#         symbol_ = specials.get(symbol) if symbol in ('nikkei', 'gold') else tran_s(symbol)
#         params = {'to': get_unix(NOW, 1), 'per_page': number,
#             'interval': interval, 'instrument': symbol_}
#         response = get(f'https://mds-api.forexfactory.com/bars?' + urlencode(params), headers=headers)
#         yield Request('https://www.google.com', meta={'data': (response.text, interval, symbol)}, dont_filter=True)

#     def parse(self, response):
#         data, interval, symbol = response.meta['data']
#         data = loads(data)
#         keys = ('data_source_id', 'interval', 'instrument')
#         results = dict()
#         for item in data.get('data'):
#             time_ = item.pop('timestamp')
#             time_ = get_unixtime(time_, divide=1, have_hour=True)
#             item = {key: round(item[key], 4) for key in item if key not in keys}
#             results.setdefault(time_, item)
#         yield {f"{symbol}_{interval}_bars": results}