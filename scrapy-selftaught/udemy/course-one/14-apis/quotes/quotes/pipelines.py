# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import logging


class SQLitePipeline(object):
    def open_spider(self, spider):
        logging.warning("OPEN SPIDER")
        self.connection = sqlite3.connect("book.db")
        try:
            self.c = self.connection.cursor()
            self.c.execute('''
                CREATE TABLE books(
                    title TEXT,
                    subject TEXT,
                    lending_identifier TEXT,
                    lending_edition TEXT
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
            INSERT INTO books (title,subject,lending_identifier,lending_edition) VALUES(?,?,?,?)
        ''', (
            item.get('title'),
            item.get('subject'),
            item.get('lending_identifier'),
            item.get('lending_edition')
        ))
        self.connection.commit()

        return item
