from scrapy import Spider, Request
from scrapy.selector import Selector
from crawldata.functions import *


class CrawlerSpider(Spider):
    name = "calendars"
    check_dirs(f"{PROJECT_PATH}/_log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/_log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
    }

    def __init__(self, *args, **kwargs): 
        super(CrawlerSpider, self).__init__(*args, **kwargs) 
        self.endpoints = kwargs.get('params').split(',')

    def start_requests(self):
        '''parsing eventid later'''
        nstart, nend = self.endpoints
        s_date, e_date = NOW - timedelta(int(nstart)), NOW + timedelta(int(nend))
        while s_date.strftime('%d%m%Y') != e_date.strftime('%d%m%Y'):
            headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------41566770301618672087425875231'
            p_date = s_date.strftime('%b %d, %Y')
            print(p_date)
            response = post('https://www.forexfactory.com/flex.php', headers=headers, data=calendata.format(p_date, p_date))
            print(response.text)
            yield Request('https://www.google.com', meta={'data': response.text}, dont_filter=True)
            s_date += timedelta(1)

    def parse(self, response):
        for item in Selector(text=response.meta['data']).xpath("//table[@class='calendar__table  ']/tr[contains(@class, 'calendar__row calendar_row')]"):
            print(item)

            # eventid = item.xpath("./@data-eventid").get()
            # time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1, have_hour=True)
            # if time_:
            #     yield {
            #         'time': time_,
            #         'event_id': eventid,
            #         'information': clean_lst(item.xpath("./td/descendant-or-self::*/text()").getall()),
            #     }