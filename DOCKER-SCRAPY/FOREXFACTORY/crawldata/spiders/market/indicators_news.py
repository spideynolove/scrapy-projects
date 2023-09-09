# from scrapy import Spider, Request
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_indicators_news"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }

#     def __init__(self, *args, **kwargs):
#         super(CrawlerSpider, self).__init__(*args, **kwargs)
#         self.endpoints = kwargs.get('params').split(',')

#     def start_requests(self):
#         symbol, interval = self.endpoints
#         params = {'instrument': tran_s(symbol), 'interval': interval, 'from': get_unix(NOW-timedelta(30), 1), 'to': get_unix(NOW+timedelta(30), 1)}
#         response = get(f'https://mds-api.forexfactory.com/indicators/news?' + urlencode(params), headers=headers)
#         yield Request('https://www.google.com', dont_filter=True, meta={'data': (response.text, symbol)})

#     def parse(self, response):
#         data, symbol = response.meta['data']
#         data = loads(data)
#         keys = ('impact_value', 'url')
#         results = dict()
#         for item in data.get('data'):
#             if item.get('impact') == 'low':
#                 continue
#             item = {key: item[key] for key in item if key not in keys}
#             time_ = item.pop('timestamp')
#             time_ = get_unixtime(time_, divide=1, have_hour=True)
#             results.setdefault(time_, item)
#         yield {f"{symbol}_news": results}