from crawldata.functions import *
from datetime import timedelta, date
from json import loads
from requests import post, get
from scrapy import Spider, Request
from scrapy.http import HtmlResponse
from urllib.parse import urlencode


class CrawlerSpider(Spider):
    name = "CalendarHist"
    check_dirs(f"{PROJECT_PATH}/log/logfile/")
    custom_settings = {
        'LOG_FILE': f"{PROJECT_PATH}/log/logfile/{SITE_PATH.name}_{name}_{LOG_TIME}.log",
        # 'DOWNLOAD_DELAY': 3,
    }

    def start_requests(self):
        '''Monthly estimation
        - another way is call at the first day of month
        - call periods by params
        '''
        # s_date = date(NOW.year, NOW.month, 1)
        # e_date = date(NOW.year, NOW.month + 1, 1)
        s_date, e_date = NOW - timedelta(0), NOW + timedelta(2)
        while s_date != e_date:
            g_date = s_date.strftime('%b %d, %Y')
            headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------41566770301618672087425875231'
            data = f'-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][idSuffix]"\r\n\r\n\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][modelData]"\r\n\r\neyJwYV9sYXlvdXRfaWQiOiJob21lcGFnZSIsInBhX2NvbXBvbmVudF9pZCI6IkNhbGVuZGFyX0NvcHkxIiwicGFfY29udHJvbHMiOiJob21lcGFnZXxDYWxlbmRhcl9Db3B5MSIsInBhX2luamVjdHJldmVyc2UiOmZhbHNlLCJwYV9oYXJkaW5qZWN0aW9uIjpmYWxzZSwicGFfaW5qZWN0YXQiOmZhbHNlLCJob21lQ2FsZW5kYXIiOnRydWUsInZpZXdpbmdUb2RheSI6ZmFsc2UsInRvZGF5RGF0ZSI6Ik1heTI0LjIwMjMiLCJ0b21vcnJvd0RhdGUiOiJNYXkyNS4yMDIzIiwicHJldkNhbExpbmsiOiJyYW5nZT1tYXkxNi4yMDIzLW1heTIzLjIwMjMiLCJuZXh0Q2FsTGluayI6InJhbmdlPWp1bjEuMjAyMy1qdW44LjIwMjMiLCJwcmV2QWx0IjoiTWF5IDE2LCAyMDIzIC0gTWF5IDIyLCAyMDIzIiwibmV4dEFsdCI6Ikp1biAxLCAyMDIzIC0gSnVuIDcsIDIwMjMiLCJuZXh0SGlkZGVuIjpmYWxzZSwicHJldkhpZGRlbiI6ZmFsc2UsInJpZ2h0TGluayI6dHJ1ZX0=\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][begindate]"\r\n\r\n{g_date}\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][enddate]"\r\n\r\n{g_date}\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][calendardefault]"\r\n\r\ntoday\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][impacts][high]"\r\n\r\nhigh\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][impacts][medium]"\r\n\r\nmedium\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][_cbarray_]"\r\n\r\n1\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][growth]"\r\n\r\ngrowth\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][inflation]"\r\n\r\ninflation\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][employment]"\r\n\r\nemployment\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][centralbank]"\r\n\r\ncentralbank\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][bonds]"\r\n\r\nbonds\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][housing]"\r\n\r\nhousing\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][sentiment]"\r\n\r\nsentiment\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][pmi]"\r\n\r\npmi\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][speeches]"\r\n\r\nspeeches\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][eventtypes][misc]"\r\n\r\nmisc\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][_cbarray_]"\r\n\r\n1\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][aud]"\r\n\r\naud\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][cad]"\r\n\r\ncad\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][chf]"\r\n\r\nchf\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][cny]"\r\n\r\ncny\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][eur]"\r\n\r\neur\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][gbp]"\r\n\r\ngbp\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][jpy]"\r\n\r\njpy\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][nzd]"\r\n\r\nnzd\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][currencies][usd]"\r\n\r\nusd\r\n-----------------------------41566770301618672087425875231\r\nContent-Disposition: form-data; name="flex[Calendar_mainCalCopy1][_cbarray_]"\r\n\r\n1\r\n-----------------------------41566770301618672087425875231--\r\n'
            response = post('https://www.forexfactory.com/flex.php', headers=headers, data=data)
            yield Request('https://www.google.com', meta={'data': (response.text, s_date)}, dont_filter=True)
            s_date += timedelta(1)

    def parse(self, response):
        data, day = response.meta['data']
        day = day.strftime('%Y-%m-%d')
        response = HtmlResponse(url="https://www.google.com", body=data, encoding='utf-8')
        for item in response.xpath("//table[@class='calendar__table  ']/tr[contains(@class, 'calendar__row calendar_row')]"):
            eventid = item.xpath("./@data-eventid").get()
            if eventid:
                event = clean_lst(item.xpath("./td[contains(@class, '__event')]/descendant-or-self::*/text()").getall())
                currency = clean_lst(item.xpath("./td[contains(@class, '__currency')]/descendant-or-self::*/text()").getall())

                params = {
                    'event_id': str(eventid),
                    'limit': '200',
                }
                response = get('https://www.forexfactory.com/calendar/events?' + urlencode(params), headers=headers)
                yield Request('https://www.google.com', callback=self.parse_detail,
                              meta={'data': (response.text, event[0], currency[0])}, dont_filter=True)

    def parse_detail(self, response):
        data, event, currency = response.meta['data']
        jdata = loads(data)
        event_data = list()
        for item in jdata.get('data').get('events')[-5:]:
            event_data.append({
                'date': get_time(item.get('date'), have_hour=False),
                'actual': get_num(item.get('actual')),
                'forecast': get_num(item.get('forecast'))
            })
        yield {event: event_data, 'currency': currency}