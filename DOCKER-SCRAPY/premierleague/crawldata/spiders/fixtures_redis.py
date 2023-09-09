from scrapy_redis.spiders import RedisSpider
from crawldata.functions import *
from crawldata.items import FixtureItem

class CrawlerSpider(RedisSpider):
    name = "fixtures_redis"
    redis_key = f'{name}:start_urls'
    redis_batch_size = 1
    max_idle_time = 7
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{MIC_PATH.name}_{name}_{LOG_TIME}.log",
        'DOWNLOAD_DELAY': 1,
    }

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
                # 'attendance': int(item.get('attendance')),
                'attendance': int(item.get('attendance')) if item.get('attendance') else '',
            })