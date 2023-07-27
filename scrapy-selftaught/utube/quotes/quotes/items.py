# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    '''
    # old item
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    # '''

    # need new item

    # can get right away
    # name = scrapy.Field()
    # wkn = scrapy.Field()
    # slug = scrapy.Field()
    # lastPrice = scrapy.Field()
    # changeToPrevDay = scrapy.Field()
    # turnover = scrapy.Field()
    # exchange = scrapy.Field()

    '''
    # take later: when go detail quote
    isin = scrapy.Field()  
    weeks52High = scrapy.Field()
    weeks52Low = scrapy.Field()
    marketCapitalisation = scrapy.Field()
    '''
    pass