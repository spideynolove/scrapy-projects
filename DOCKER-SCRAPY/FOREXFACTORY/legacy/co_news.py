from scrapy import Spider, Request
from crawldata.functions import *
from requests import get, post
from scrapy.http import HtmlResponse


class CrawlerSpider(Spider):
    name = "News"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
    }

    headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'
    params = {'more': '1',}

    def start_requests(self):
        # Latest news
        data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][idSuffix]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJuZXdzIiwicGFfY29tcG9uZW50X2lkIjoiTmV3c0xlZnRPbmUiLCJwYV9jb250cm9scyI6Im5ld3N8TmV3c0xlZnRPbmUiLCJwYV9pbmplY3RyZXZlcnNlIjpmYWxzZSwicGFfaGFyZGluamVjdGlvbiI6ZmFsc2UsInBhX2luamVjdGF0IjpmYWxzZX0=\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][stream][]"\r\n\r\n1\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][news]"\r\n\r\nall\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][format]"\r\n\r\nheadline\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][items]"\r\n\r\n15\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsLeft1][sort]"\r\n\r\nlatest\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': response.text}, dont_filter=True)

    def parse(self, response):
        data = response.meta['data']
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        results = {'latest': dict()}
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['latest'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Hottest stories
        data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][idSuffix]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJuZXdzIiwicGFfY29tcG9uZW50X2lkIjoiTmV3c1JpZ2h0T25lIiwicGFfY29udHJvbHMiOiJuZXdzfE5ld3NSaWdodE9uZSIsInBhX2luamVjdHJldmVyc2UiOmZhbHNlLCJwYV9oYXJkaW5qZWN0aW9uIjpmYWxzZSwicGFfaW5qZWN0YXQiOmZhbHNlfQ==\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][news]"\r\n\r\nall\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][format]"\r\n\r\nlarge\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][items]"\r\n\r\n3\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight1][sort]"\r\n\r\nhottest\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': (response.text, results)}, dont_filter=True, callback=self.parse_hottest)

    def parse_hottest(self, response):
        data, results = response.meta['data']
        results['hottest'] = dict()
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['hottest'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Most Viewed 12H
        data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][idSuffix]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJuZXdzIiwicGFfY29tcG9uZW50X2lkIjoiTmV3c1JpZ2h0VGhyZWUiLCJwYV9jb250cm9scyI6Im5ld3N8TmV3c1JpZ2h0VGhyZWUiLCJwYV9pbmplY3RyZXZlcnNlIjpmYWxzZSwicGFfaGFyZGluamVjdGlvbiI6ZmFsc2UsInBhX2luamVjdGF0IjpmYWxzZX0=\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][news]"\r\n\r\n8\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][format]"\r\n\r\nthreads\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][items]"\r\n\r\n3\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][sort]"\r\n\r\nmostviewed\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight3][period]"\r\n\r\nlast12h\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': (response.text, results)}, dont_filter=True, callback=self.parse_most_viewed)

    def parse_most_viewed(self, response):
        data, results = response.meta['data']
        results['most_viewed'] = dict()
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['most_viewed'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Latest Fundamental Analysis
        data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][idSuffix]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJuZXdzIiwicGFfY29tcG9uZW50X2lkIjoiTmV3c1JpZ2h0VHdvIiwicGFfY29udHJvbHMiOiJuZXdzfE5ld3NSaWdodFR3byIsInBhX2luamVjdHJldmVyc2UiOmZhbHNlLCJwYV9oYXJkaW5qZWN0aW9uIjpmYWxzZSwicGFfaW5qZWN0YXQiOmZhbHNlfQ==\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][news]"\r\n\r\n107\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][format]"\r\n\r\nthreads\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][items]"\r\n\r\n3\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][sort]"\r\n\r\nmostviewed\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight2][period]"\r\n\r\nlast12h\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': (response.text, results)}, dont_filter=True, callback=self.parse_latest_fa)

    def parse_latest_fa(self, response):
        data, results = response.meta['data']
        results['latest_fa'] = dict()
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['latest_fa'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        # Latest Technical Analysis
        data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][idSuffix]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJuZXdzIiwicGFfY29tcG9uZW50X2lkIjoiTmV3c1JpZ2h0Rm91ciIsInBhX2NvbnRyb2xzIjoibmV3c3xOZXdzUmlnaHRGb3VyIiwicGFfaW5qZWN0cmV2ZXJzZSI6ZmFsc2UsInBhX2hhcmRpbmplY3Rpb24iOmZhbHNlLCJwYV9pbmplY3RhdCI6ZmFsc2V9\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][news]"\r\n\r\n89\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][format]"\r\n\r\nlarge\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][items]"\r\n\r\n2\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[News_newsRight4][sort]"\r\n\r\nlatest\r\n-----------------------------48222048032047603611657549096--\r\n'
        response = post('https://www.forexfactory.com/flex.php', params=self.params, headers=headers, data=data)
        yield Request('https://www.google.com', meta={'data': (response.text, results)}, dont_filter=True, callback=self.parse_latest_ta)

    def parse_latest_ta(self, response):
        data, results = response.meta['data']
        results['latest_ta'] = dict()
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//ul[@class='body flexposts']/li"):
            time_ = get_unixtime(item.xpath("./@data-timestamp").get(), divide=1)
            results['latest_ta'].setdefault(time_, clean_lst(item.xpath("./descendant-or-self::*/text()").getall())[0])

        yield results