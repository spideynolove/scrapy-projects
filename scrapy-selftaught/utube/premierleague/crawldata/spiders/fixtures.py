from scrapy import Spider, Request
from crawldata.functions import *
from urllib.parse import urlencode
from json import loads


class CrawlerSpider(Spider):
    name = "Fixtures"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }

    def start_requests(self):
        headers['User-Agent'] = random_user_agent()
        headers['Origin'] = 'https://www.premierleague.com'
        url = 'https://footballapi.pulselive.com/football/fixtures?' + urlencode(fixturesparams)
        yield Request(url, headers=headers, meta={'page': fixturesparams.get('page')})

    def parse(self, response):
        page = int(response.meta['page'])
        data = loads(response.text)
        for item in data.get('content'):
            yield {
                'Week': int(item.get('gameweek').get('gameweek')),
                'Season': item.get('gameweek').get('compSeason').get('label'),
                'Host': {
                    'Name': item.get('teams')[0].get('team').get('name'),
                    'Score': int(item.get('teams')[0].get('score')),
                },
                'Guest': {
                    'Name': item.get('teams')[1].get('team').get('name'),
                    'Score': int(item.get('teams')[1].get('score')),
                },
                'Stadium': {
                    'Name': item.get('ground').get('name'),
                    'City': item.get('ground').get('city'),
                },
                'Attendance': int(item.get('attendance')),
            }
        if data.get('content'):
            page += 1
            fixturesparams['page'] = str(page)
            url = 'https://footballapi.pulselive.com/football/fixtures?' + urlencode(fixturesparams)
            yield Request(url, headers=headers, meta={'page': page})