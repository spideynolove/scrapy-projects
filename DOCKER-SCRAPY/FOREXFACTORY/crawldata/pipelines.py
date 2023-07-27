import pymongo
from bson.objectid import ObjectId
import logging
import json
from crawldata.functions import *
from configparser import ConfigParser
config = ConfigParser()


class CrawldataPipeline(object):
    def open_spider(self, spider):
        logging.warning("OPEN SPIDER")
        if USE_LOCAL_MONGO:
            self.client = pymongo.MongoClient('localhost', 27017)
            self.db = self.client["BABYPIPS"]
        else:
            config.read(f"{SITE_PATH}/login/accounts.ini")
            config_data = config["MONGO"]
            self.client = pymongo.MongoClient(f"mongodb+srv://{config_data['username']}:{config_data['password']}@cluster0.txls7.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client["BABYPIPS"]

    def process_item(self, item, spider):
        # pseudo code
        # daily -> unique
        # settings
        # hour
        
        # cursor = self.db[spider.name].find()
        # for each_doc in cursor:
        #     print(each_doc)

        # add new
        with open(f'{SITE_PATH}/mong_id/time_id.json') as ftime:
            id_json = json.loads(ftime.read())
        id_json["_id"] = ObjectId(id_json["_id"])
        item = {**id_json, **item}

        self.db[spider.name].insert_one(item)

        # update
        pass

    def close_spider(self, spider):
        logging.warning("CLOSE SPIDER")
        self.client.close()
