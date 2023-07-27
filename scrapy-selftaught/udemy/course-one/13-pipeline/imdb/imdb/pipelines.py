# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pymongo
import sqlite3
import logging
from dotenv import load_dotenv


class MongoPipeline(object):
    collection_name = "best_movies"

    def open_spider(self, spider):
        logging.warning("OPEN SPIDER")
        load_dotenv()
        USER = os.getenv('user')
        PWD = os.getenv('password')


        self.client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PWD}@cluster0.txls7.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        logging.warning("CLOSE SPIDER")
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item


class SQLitePipeline(object):
    def open_spider(self, spider):
        logging.warning("OPEN SPIDER")
        self.connection = sqlite3.connect("imdb.db")
        try:
            self.c = self.connection.cursor()
            self.c.execute('''
                CREATE TABLE best_movies(
                    title TEXT,
                    year TEXT,
                    duration TEXT,
                    genre TEXT,
                    rating TEXT,
                    movie_url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        logging.warning("CLOSE SPIDER")
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO best_movies (title,year,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?)
        ''', (
            item.get('title'),
            item.get('year'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url')
        ))
        self.connection.commit()

        return item
