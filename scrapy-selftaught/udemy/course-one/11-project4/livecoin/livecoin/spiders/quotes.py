import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    quotes_urls = 'http://quotes.toscrape.com/js'

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(1))

            splash:set_viewport_full()

            return {
                image = splash:png(),
                html = splash:html(),
            }
        end

    '''

    def start_requests(self):
        yield SplashRequest(url=self.quotes_urls, callback=self.parse,
                            endpoint='execute', args={
                                'lua_source': self.script
                            })

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote text': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//span[2]/small[@class='author']/text()").get(),
                'tags': quote.xpath(".//div[@class='tags']/a/text()").getall()

            }
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            absolute_url = f"http://quotes.toscrape.com{next_page}"
            yield SplashRequest(url=absolute_url, callback=self.parse, endpoint='execute', args={
                'lua_source': self.script
            })
