import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['web.archive.org']
    start_urls = [
        "https://web.archive.org/web/20200116052415/https://www.livecoin.net/en"]
    coin_url = "https://web.archive.org/web/20200116052415/https://www.livecoin.net/en"

    def __init__(self):
        firefox_path = which("geckodriver")
        driver = webdriver.Firefox(executable_path=firefox_path)
        driver.set_window_size(1920, 1080)

        driver.get(self.coin_url)
        run_tab = driver.find_element(
            "xpath", "(//div[@class='filterPanelItem___2z5Gb '])[3]")
        run_tab.click()
        # timeout = 5
        try:
            # temp = driver.find_element("xpath", "//div[contains(@class, 'tableRow___3EtiS')]")
            # WebDriverWait(driver, timeout).until(temp)
            self.html = driver.page_source
            driver.close()
        except TimeoutException:
            print("Timed out waiting for page to load")

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'tableRow___3EtiS')]"):
            yield {
                'currency_pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get(),
                'last_price': currency.xpath(".//div[3]/span/text()").get(),
                'change(24h)': currency.xpath(".//div[4]/span/span/text()").get(),
                'high(24h)': currency.xpath(".//div[5]/span/text()").get(),
                'low(24h)': currency.xpath(".//div[6]/span/text()").get(),
            }
