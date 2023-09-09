from scrapy import Request, Spider
from crawldata.functions import *
from crawldata.items import FixtureItem


class CrawlerSpider(Spider):
    name = "fixtures"
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }
    base = 'https://footballapi.pulselive.com/football/fixtures?{}'

    def __init__(self, *args, **kwargs): 
        super(CrawlerSpider, self).__init__(*args, **kwargs) 
        fixparams['teams'] = kwargs.get('teams')

    def start_requests(self):
        open(f'{MIC_PATH}/{self.name}.json', 'w').close()
        yield Request(self.base.format(urlencode(fixparams)), meta={'page': fixparams.get('page')})

    def parse(self, response):
        page = int(response.meta['page'])
        data = loads(response.text)
        for item in data.get('content'):
            yield FixtureItem({
                'week': int(item.get('gameweek').get('gameweek')),
                'season': item.get('gameweek').get('compSeason').get('label'),
                'host': {
                    'name': item.get('teams')[0].get('team').get('name'),
                    'score': int(item.get('teams')[0].get('score')),
                },
                'guest': {
                    'name': item.get('teams')[1].get('team').get('name'),
                    'score': int(item.get('teams')[1].get('score')),
                },
                'stadium': {
                    'name': item.get('ground').get('name'),
                    'city': item.get('ground').get('city'),
                },
                # 'attendance': int(item.get('attendance')),
                'attendance': int(item.get('attendance')) if item.get('attendance') else '',
            })
        if data.get('content'):
            fixparams['page'] = str(page+1)
            yield Request(self.base.format(urlencode(fixparams)), meta={'page': page})