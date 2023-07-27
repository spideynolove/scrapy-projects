import scrapy
from scrapy.exceptions import CloseSpider
import json


class BooksSpider(scrapy.Spider):
    name = 'books'
    offset, limit, STEP = 0, 120, 100

    allowed_domains = ['openlibrary.org']
    start_urls = [
        f'http://openlibrary.org/subjects/picture_books.json?limit={limit}']

    def parse(self, response):
        resp = json.loads(response.body)

        # if response.status == 500:
        # if self.offset > int(resp.get('ebook_count')):
        if self.offset > 50:
            raise CloseSpider('Already visit last page...')

        ebooks = resp.get('works')
        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'subject': ebook.get('subject')[0], # can't push list to sqlite column
                'lending_identifier': ebook.get('lending_identifier'),
                'lending_edition': ebook.get('lending_edition'),
            }

        self.offset += self.STEP
        yield scrapy.Request(
            url=f'http://openlibrary.org/subjects/picture_books.json?limit={self.limit}&offset={self.offset}',
            callback=self.parse
        )
