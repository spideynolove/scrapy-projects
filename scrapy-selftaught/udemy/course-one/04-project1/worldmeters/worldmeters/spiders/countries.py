# -*- coding: utf-8 -*-
import scrapy

URL = 'https://www.worldometers.info/world-population/population-by-country/'


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    start_urls = [URL]

    def parse(self, resp):
        for country in resp.xpath("//td/a"):
            # if name == 'China':
            yield resp.follow(url=country.xpath(".//@href").get(),
                              callback=self.parse_country,
                              meta={"country_name": country.xpath(".//text()").get()})

    def parse_country(self, resp):
        # print(resp.url)
        country_name = resp.request.meta["country_name"]
        temp = dict()
        for row in resp.xpath("//*[contains(@class, 'table-striped')]/tbody/tr"):
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            temp.setdefault(year, population)
        yield {
            country_name: temp,
        }
