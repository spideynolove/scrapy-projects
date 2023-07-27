# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    movie_url = scrapy.Field()
    pass
