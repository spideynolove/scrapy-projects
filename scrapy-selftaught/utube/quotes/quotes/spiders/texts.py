import scrapy
import datetime
import hashlib
import ast
import json

from datetime import (
    datetime, timezone, date
)

from urllib.parse import urlencode
from scrapy.http import JsonRequest


class TextSpider(scrapy.Spider):
    name = "total"
    url = "https://www.boerse-frankfurt.de/equities/search"
    api_url = "https://api.boerse-frankfurt.de/v1/search/equity_search"
    stock_url = 'https://www.boerse-frankfurt.de/equity/{}/price-history/historical-prices-and-volumes'

    json_request = {
        'indices': [],
        'regions': [],
        'countries': [],
        'sectors': [],
        'types': [],
        'forms': [],
        'segments': [],
        'markets': [],
        'stockExchanges': [],
        'lang': 'en',
        'offset': 0,
        'limit': 100,
        'sorting': 'TURNOVER',
        'sortOrder': 'DESC',
    }

    def generate_headers(self, url):
        '''Fake important header changeable params'''
        # hungnm17 get this secret key from debugging process
        salt = "w4ivc1ATTGta6njAZzMbkL3kJwxMfEAKDa3MNr"

        current_time = datetime.now(tz=timezone.utc)
        client_date = (current_time
                       .isoformat(timespec="milliseconds")
                       .replace("+00:00", "Z")
                       )
        client_traceid = hashlib.md5(
            (client_date + url + salt).encode("utf-8")
        )
        security = hashlib.md5(
            current_time.strftime("%Y%m%d%H%M").encode("utf-8")
        )

        return {
            "Client-Date": client_date,
            "X-Client-TraceId": client_traceid.hexdigest(),
            "X-Security": security.hexdigest()
        }

    def handle_resp_text(self, response):
        # data must not have null vals
        data = response.text.replace(
            'null', '"null"') if 'null' in response.text else response.text
        return ast.literal_eval(data)

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse_api)

    def parse_api(self, response):
        try:
            # total = response.xpath(
            #     '//span[@class="ng-star-inserted"]/text()').get()

            total = response.xpath(
                "/html/body/app-root/app-wrapper/div/div[2]/app-equity-search/div/div[2]/div/span/text()").get()
            total = int(total.replace(",", ""))

            for page in range(total):
                if page == 2:
                    break
                self.json_request["offset"] = str(
                    int(self.json_request['limit'])*page)

                # each page of 100 ticker come here
                yield JsonRequest(self.api_url, callback=self.parse_search,
                                  headers=self.generate_headers(self.api_url),
                                  data=self.json_request, method="POST")

        except:
            print("An exception occurred: Wrong URL cause wrong text number")

    def parse_search(self, response):
        json_ret = self.handle_resp_text(response)['data']
        for count, quote in enumerate(json_ret):
            if count == 2:
                break

            # each ticker in 1 page come here
            yield scrapy.Request(self.stock_url.format(quote["slug"]),
                                 self.parse_price,
                                 meta={"wkn": quote["wkn"],
                                       "isin": quote["isin"],
                                       "exchange": quote["overview"]["exchange"]})

    def parse_price(self, response):
        # ticker = response.xpath(
        #     '//span[@class="ng-star-inserted"][1]/text()').get()

        try:
            ticker = response.xpath(
                "/html/body/app-root/app-wrapper/div/div[2]/app-equity/div[1]/div/app-widget-datasheet-header/div/div/div[1]/div/div[2]/div/span[3]/text()").get()
            ticker = ticker.split(": ")[1]

            start_date = date(2021, 7, 24)
            end_date = date(2022, 7, 24)

            # estimating number of business date
            daydiff = end_date.weekday() - start_date.weekday()
            nums_date = ((end_date-start_date).days - daydiff) / 7 * 5 + \
                min(daydiff, 5) - (max(end_date.weekday() - 4, 0) % 5)

            params = {
                'limit': '100',
                'offset': '0',
                'isin': response.meta["isin"],
                'mic': response.meta["exchange"],
                'minDate': start_date.strftime('%Y-%m-%d'),
                'maxDate': end_date.strftime('%Y-%m-%d'),

                'cleanSplit': 'false',
                'cleanPayout': 'false',
                'cleanSubscriptionRights': 'false',
            }

            for page in range(int(nums_date)):
                if page == 2:
                    break
                # next page logic
                params["offset"] = str(int(params['limit'])*page)
                ticker_url = "https://api.boerse-frankfurt.de/v1/data/price_history?" + \
                    urlencode(params)

                # each page of 100 days come here
                yield scrapy.Request(ticker_url, callback=self.parse,
                                     headers=self.generate_headers(ticker_url), method="GET",
                                     meta={"wkn": response.meta["wkn"],
                                           "isin": response.meta["isin"],
                                           "exchange": response.meta["exchange"]})
        except:
            print("An exception occurred: Wrong URL cause wrong text number")

    def parse(self, response):
        price_json = json.loads(response.text)['data']

        yield None
