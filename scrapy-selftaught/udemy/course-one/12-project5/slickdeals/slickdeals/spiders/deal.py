import time
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys


class SlickdealsSpider(scrapy.Spider):
    name = 'deals'

    def start_requests(self):
        yield SeleniumRequest(
            # url="https://slickdeals.net/computer-deals",
            url="https://duckduckgo.com",
            wait_time=1,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        # img = response.meta['screenshot']
        # with open("screenshot.png", 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element(
            "xpath", "//input[@id='search_form_input_homepage']")
        search_input.send_keys('blender low poly art')
        search_input.send_keys(Keys.ENTER)

        driver.find_element(
            "xpath", "//a[@data-zci-link='images']").click()

        # wait = WebDriverWait(driver, 10)
        time.sleep(2)
        # driver.save_screenshot('lowpoly.png')

        html = driver.page_source
        resp_obj = Selector(text=html)
