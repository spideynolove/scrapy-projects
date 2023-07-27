import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['web.archive.org']
    coin_url = "https://web.archive.org/web/20200116052415/https://www.livecoin.net/en"

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            local url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))

            local run_tab = assert(splash:select_all(".filterPanelItem___2z5Gb "))
            run_tab[4]:mouse_click()
            assert(splash:wait(1))

            -- local show_more = assert(splash:select(".button-red"))
            -- show_more:mouse_click()
            -- assert(splash:wait(2))
            
            splash:set_viewport_full()
            return {
                image = splash:png(),
                html = splash:html(),
            }
        end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.coin_url, callback=self.parse,
                            endpoint="execute", args={
                                "lua_source": self.script
                            })

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class, 'tableRow___3EtiS')]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get(),
                'last_price': currency.xpath(".//div[3]/span/text()").get(),
                'change(24h)': currency.xpath(".//div[4]/span/span/text()").get(),
                'high(24h)': currency.xpath(".//div[5]/span/text()").get(),
                'low(24h)': currency.xpath(".//div[6]/span/text()").get(),
            }
