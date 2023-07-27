# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider


class BestmoviesSpider(CrawlSpider):
    name = 'bestmovies'
    allowed_domains = ['imdb.com']
    imdb_url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url=self.imdb_url, callback=self.parse_item, headers={
            'User-Agent': self.user_agent
        })

    def parse_item(self, response):
        for item in response.xpath("(//div[@class='lister-item-content'])"):
            yield {
                "title": item.xpath(".//h3[@class='lister-item-header']/a/text()").get(),
                "year": re.findall(r'\d+', item.xpath(".//h3[@class='lister-item-header']/span[2]/text()").get())[0],
                "duration": item.xpath(".//p[1]/span[@class='runtime']/text()").get(),
                "genre": item.xpath("normalize-space(.//p[1]/span[@class='genre']/text())").get(),
                "rating": item.xpath(".//div[@class= 'ratings-bar']/div[1]/@data-value").get(),
                "movie_url": response.urljoin(item.xpath(".//h3[@class='lister-item-header']/a/@href").get()),
            }
        next_page = response.xpath(
            "(//a[@class='lister-page-next next-page'])[2]/@href").get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_item, headers={
                'User-Agent': self.user_agent
            })
