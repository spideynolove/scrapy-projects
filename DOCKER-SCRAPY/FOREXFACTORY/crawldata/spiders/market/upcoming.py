# from scrapy import Spider, Request
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_upcoming"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }


#     def __init__(self, *args, **kwargs): 
#         super(CrawlerSpider, self).__init__(*args, **kwargs) 
#         self.endpoints = kwargs.get('params').split(',')

#     def start_requests(self):
#         symbol, limit = self.endpoints
#         url = f'https://www.forexfactory.com/upcoming/{symbol.upper()}?' + urlencode({'limit': limit, })
#         headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
#         response = get(url, headers=headers)
#         yield Request('https://www.google.com', meta={'data': (response.text, symbol)}, dont_filter=True)

#     def parse(self, response):
#         data, symbol = response.meta['data']
#         data = loads(data)
#         keys = ('time_mask', 'in_time', 'impact_value', 'impact_icon_class', 'event_url', 'details_url')
#         results = list()
#         for item in data.get('events'):
#             if item.get('impact_name') == 'low':
#                 continue
#             item = {key: item[key] for key in item if key not in keys}
#             time_ = item.pop('dateline')
#             time_ = get_unixtime(time_, divide=1, have_hour=True)
#             results.append({'time': time_, **item})
#         yield {f"{symbol}_upcoming": results}