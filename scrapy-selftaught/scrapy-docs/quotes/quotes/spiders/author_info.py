import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        self.logger.info(
            'parse:: A response from %s just arrived!', response.url)

        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        # next handle
        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        self.logger.info(
            'parse_author:: A response from %s just arrived!', response.url)

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
