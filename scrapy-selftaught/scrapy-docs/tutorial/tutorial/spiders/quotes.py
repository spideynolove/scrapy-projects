import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     # allowed_domains = ['quotes.toscrape.com']
#     # start_urls = ['http://quotes.toscrape.com/']

#     def start_requests(self):
#         urls = [
#             'https://quotes.toscrape.com/page/1/',
#             'https://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')


# ----------------------------------------------------------------------------
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     # all we want is here
#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#         'https://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         print(f"HUNG page: {page}")
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')


# ----------------------------------------------------------------------------

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#         'https://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }
# ----------------------------------------------------------------------------


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }

#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             print(f"HUNG next_page: {next_page}")
#             yield scrapy.Request(next_page, callback=self.parse)
# ----------------------------------------------------------------------------
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('span small::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }

#         # next_page = response.css('li.next a::attr(href)').get()
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)
# #             yield scrapy.Request(next_page, callback=self.parse)

#         anchors = response.css('ul.pager a')    # href attribute automatically
#         print(f"HUNG anchors: {anchors}")
#         yield from response.follow_all(anchors, callback=self.parse)
# ----------------------------------------------------------------------------


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
            # HUNG url tag: https://quotes.toscrape.com/tag/humor
            print(f"HUNG url tag: {url}")   
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
