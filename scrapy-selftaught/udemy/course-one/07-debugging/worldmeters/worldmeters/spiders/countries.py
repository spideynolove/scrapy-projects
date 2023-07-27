# -*- coding: utf-8 -*-
import scrapy
import logging
# from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser


class CountriesSpider(scrapy.Spider):
    name = 'countries'

    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, resp):
        # countries = resp.xpath("//td/a")
        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     link = country.xpath(".//@href").get()
        #     yield resp.follow(url=link, callback=self.parse_country, meta={"country_name": name})

        # for test
        yield resp.follow(url='https://www.worldometers.info/world-population/afghanistan-population/',
                          callback=self.parse_country, meta={"country_name": 'China'})

    def parse_country(self, resp):
        # logging.info(resp.status)
        # inspect_response(resp, self)
        # open_in_browser(resp)

        country_name = resp.request.meta["country_name"]
        temp = dict()
        for row in resp.xpath("//*[contains(@class, 'table-striped')]/tbody/tr"):
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            temp.setdefault(year, population)
        yield {
            country_name: temp,
        }
