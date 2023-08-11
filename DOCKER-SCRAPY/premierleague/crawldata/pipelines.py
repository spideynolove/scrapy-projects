from crawldata.functions import *


class CrawldataPipeline:
    collection = 'items'

    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.collection = spider.name
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

        # Start with a clean database
        self.db[self.collection].delete_many({})

        # update not clean

    def close_spider(self, spider):
        check_dirs(f"{PROJECT_PATH}/log/summary/")
        log_file = f"{PROJECT_PATH}/log/summary/{MIC_PATH.name}_{spider.name}_{LOG_TIME}.json"
        SUMMARY = spider.crawler.stats.get_stats()
        SUMMARY['start_time'] = SUMMARY['start_time'].strftime('%Y-%m-%dT%H-%M-%S')
        with open(log_file, "w", encoding='utf-8') as f:
            f.write(dumps(SUMMARY))
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        return item