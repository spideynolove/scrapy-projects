# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    # url = "https://www.worldometers.info/world-population/population-by-country"
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    # def start_requests(self):
    #     yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div/h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        self.logger.info(f'A response from {response.url} just arrived!')
        self.logger.info(f'Response title: {title}')
        self.logger.info(f'Response country: {countries}')
        
        yield {
            "title": title,
            "countries": countries,
        }
