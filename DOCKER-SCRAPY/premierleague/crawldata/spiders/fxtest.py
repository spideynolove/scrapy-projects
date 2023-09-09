from scrapy import Request, Spider
from crawldata.functions import *
from crawldata.items import FixtureItem


class CrawlerSpider(Spider):
    name = "fxtest"
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }

    def start_requests(self):
        open(f'{MIC_PATH}/{self.name}.json', 'w').close()
        url = 'https://footballapi.pulselive.com/football/fixtures?comps=1&pageSize=20&sort=desc&statuses=C&altIds=true&compSeasons=489&page=0&teams=10'
        yield Request(url)

    def parse(self, response):
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
                'attendance': int(item.get('attendance')) if item.get('attendance') else '',
            })