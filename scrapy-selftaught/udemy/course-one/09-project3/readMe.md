
# new archive link:

- [imdb_archive](http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating)

# project link

- [main_imdb](https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc)

# Rule and LinkExtractor

# add user-agent

# using CrawlSpider only

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
    rules = (
        # handle items
        Rule(LinkExtractor(restrict_xpaths=(
            "//h3[@class='lister-item-header']/a")),
            callback='parse_item', follow=True,
        ),
        # handle next
        Rule(LinkExtractor(restrict_xpaths=(
            "(//a[@class='lister-page-next next-page'])[2]")),
        ),
    )

    def parse_item(self, resp):
        pass