# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestmoviesSpider(CrawlSpider):
    name = 'bestmovies'
    start_urls = [
        'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    rules = (
        Rule(LinkExtractor(restrict_xpaths=(
            "//h3[@class='lister-item-header']/a")),
            callback='parse_item', follow=True,
            # process_request='set_user_agent'
        ),
        Rule(LinkExtractor(restrict_xpaths=(
            "(//a[@class='lister-page-next next-page'])[2]")),
            # process_request='set_user_agent'
        ),
    )

    def parse_item(self, resp):
        yield {
            "title": resp.xpath("//h1[@data-testid='hero-title-block__title']/text()").get(),
            "year": resp.xpath("(//span[@class='sc-8c396aa2-2 itZqyK'])[1]/text()").get(),
            "duration": ''.join(resp.xpath("//ul[@data-testid='hero-title-block__metadata']/li[3]/text()").getall()),
            "genre": resp.xpath("//li[@data-testid= 'storyline-genres']/div/ul/li/a/text()").get(),
            "rating": resp.xpath("(//div[@data-testid = 'hero-rating-bar__aggregate-rating__score']/span)[1]/text()").get(),
            "movie_url": resp.url,
        }
