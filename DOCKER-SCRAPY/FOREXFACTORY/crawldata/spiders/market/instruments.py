# from scrapy import Spider, Request
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_instruments"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }

#     def __init__(self, *args, **kwargs): 
#         super(CrawlerSpider, self).__init__(*args, **kwargs) 
#         self.endpoints = kwargs.get('params').split(',')
        
#     def start_requests(self):
#         endpoints = [specials.get(symbol) if symbol in ('nikkei', 'gold') else tran_s(symbol) for symbol in self.endpoints]
#         endpoints = {'instruments': ','.join(endpoints), }
#         url = f"https://mds-api.forexfactory.com/instruments?{urlencode(endpoints)}"
#         yield Request(url, headers=headers)

#     def parse(self, response):
#         data = loads(response.text)
#         for item in data.get('data'):
#             instrument = item.get('instrument').get('name').replace('/', '').lower()
#             yield {f"{instrument}": item.get('metrics')}