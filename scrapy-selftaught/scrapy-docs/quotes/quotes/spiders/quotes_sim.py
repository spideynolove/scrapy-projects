import scrapy


class QuotesSpider(scrapy.Spider):
    '''no need start request, just using start_urls'''
    name = "quotes"
    start_urls = [
        # 'https://quotes.toscrape.com/page/1/',
        # 'https://quotes.toscrape.com/page/2/',
        'https://quotes.toscrape.com'
    ]

    def parse(self, response):
        ######################################################
        # page = response.url.split("/")[-2]
        # filename = f'quotes-sim-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        ######################################################
        # for quote in response.css("div.quote"):
        #     text = quote.css("span.text::text").get()
        #     author = quote.css("small.author::text").get()
        #     tags = quote.css("div.tags a.tag::text").getall()
        #     print(dict(text=text, author=author, tags=tags))
        ######################################################
        # Extracting data in our spider
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        ######################################################
        # # Normal way
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     # yield scrapy.Request(next_page, callback=self.parse)
        #     ######################################################
        #     # Following links
        #     yield response.follow(next_page, callback=self.parse)
        ######################################################
        # # Another way
        # for href in response.css('ul.pager a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)
        #     ######################################################
        # for a in response.css('ul.pager a'):
        #     yield response.follow(a, callback=self.parse)

        ######################################################
        # To create multiple requests from an iterable
        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)
