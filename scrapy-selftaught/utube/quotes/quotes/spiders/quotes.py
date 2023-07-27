import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    url = 'https://www.boerse-frankfurt.de/indices/tecdax'

    def start_requests(self):
        yield scrapy.Request(self.url)

    def parse(self, response):
        # name = response.xpath('//h1[@class="instrument-name"]/text()').get()
        temp_code = response.xpath("//span[contains(text(), 'ISIN:')]/following-sibling::span[1]/text()").get()
        temp_code2 = response.xpath("//span[contains(text(), 'WKN:')]/following-sibling::span[1]/text()").get()
        temp_code3 = response.xpath("//span[contains(text(), 'ISIN:')]/following-sibling::span[3]/text()").get()
        print(f'HUNG NAME: {temp_code}, {temp_code2}, {temp_code3}')