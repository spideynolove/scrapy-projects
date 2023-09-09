# from scrapy import Spider, Request
# from scrapy.selector import Selector
# from crawldata.functions import *


# class CrawlerSpider(Spider):
#     name = "market_news"
#     check_dirs(f"{PROJECT_PATH}/_log/logfile/")
#     custom_settings = {
#         'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
#     }
#     headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
#     nparams = {'more': '2',}

#     def start_requests(self):
#         for type_, data in NEWS.items():
#             data = data.format(self.quote)
#             response = post('https://www.forexfactory.com/flex.php', params=self.nparams, headers=headers, data=data)
#             yield Request('https://www.google.com', meta={'data': (response.text, self.quote, type_)}, dont_filter=True)

#     def parse(self, response):
#         data, symbol, type_ = response.meta['data']
#         li_selector = Selector(text=data).xpath("//ul[@class='body flexposts']/li")
#         results = dict()
#         for item in li_selector:
#             time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1, have_hour=True)
#             results.setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])
#         yield {f"{symbol}_{type_}_news": results}