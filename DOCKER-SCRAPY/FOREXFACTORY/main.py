from requests import get, post
from crawldata.functions import *
from datetime import datetime, date, timedelta
from urllib.parse import urlencode

# # params = {
# #     # 'event_id': '133407',
# #     'event_id': '130946',
# #     'limit': '200',
# # }

# # response = get('https://www.forexfactory.com/calendar/events',
# #                params=params,
# #                headers=headers)

# SYMBOLS = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CHF',
#            'USD/CAD', 'AUD/USD', 'NZD/USD', 'GBP/JPY']

# ret = list()
# for test in SYMBOLS:
#     test = test.replace('/', '%2F')
#     subfix = (",12,M30", ",24,H1", ",12,H4")
#     subfix = [f"{a}{b}" for a, b in zip([test,]*len(subfix), subfix)]
#     tmp = ("requests[]=", )
#     subfix = [f"{a}{b}" for a, b in zip(tmp*len(subfix), subfix)]
#     ret.append(subfix)

# outcome = '&'.join(flatten(ret))
# # print(outcome)
# # outcome = 'requests[]=EURUSD,12,M30&requests[]=EURUSD,24,H1&requests[]=EURUSD,12,H4&requests[]=AUDUSD,12,M30&requests[]=AUDUSD,24,H1&requests[]=AUDUSD,12,H4&requests[]=NZDUSD,12,M30&requests[]=NZDUSD,24,H1&requests[]=NZDUSD,12,H4&requests[]=USDJPY,12,M30&requests[]=USDJPY,24,H1&requests[]=USDJPY,12,H4&requests[]=USDCHF,12,M30&requests[]=USDCHF,24,H1&requests[]=USDCHF,12,H4&requests[]=USDCAD,12,M30&requests[]=USDCAD,24,H1&requests[]=USDCAD,12,H4&requests[]=GBPUSD,12,M30&requests[]=GBPUSD,24,H1&requests[]=GBPUSD,12,H4&requests[]=EURAUD,12,M30&requests[]=EURAUD,24,H1&requests[]=EURAUD,12,H4&requests[]=EURNZD,12,M30&requests[]=EURNZD,24,H1&requests[]=EURNZD,12,H4&requests[]=EURCAD,12,M30&requests[]=EURCAD,24,H1&requests[]=EURCAD,12,H4&requests[]=EURCHF,12,M30&requests[]=EURCHF,24,H1&requests[]=EURCHF,12,H4&requests[]=EURJPY,12,M30&requests[]=EURJPY,24,H1&requests[]=EURJPY,12,H4&requests[]=EURGBP,12,M30&requests[]=EURGBP,24,H1&requests[]=EURGBP,12,H4&requests[]=GBPAUD,12,M30&requests[]=GBPAUD,24,H1&requests[]=GBPAUD,12,H4&requests[]=GBPNZD,12,M30&requests[]=GBPNZD,24,H1&requests[]=GBPNZD,12,H4&requests[]=GBPCAD,12,M30&requests[]=GBPCAD,24,H1&requests[]=GBPCAD,12,H4&requests[]=GBPCHF,12,M30&requests[]=GBPCHF,24,H1&requests[]=GBPCHF,12,H4&requests[]=GBPJPY,12,M30&requests[]=GBPJPY,24,H1&requests[]=GBPJPY,12,H4'
# response = get('https://mds-api.forexfactory.com/bars/aggregate?' + outcome,
#                headers=headers,
#                )

params = {
    'content': 'positions',
    'do': 'positions_graph_data',
    'currency': 'EURUSD',
    'interval': 'D1',
    'limit': '200',
}

response = get('https://www.forexfactory.com/explorerapi.php', params=params, 
            #    cookies=cookies, 
               headers=headers)

print(response.text)


# -----------------------------------------------------------------------------
# upcoming
import requests

cookies = {
    'fflastvisit': '1682255256',
    'fflastactivity': '0',
    'ffsettingshash': '4ba71072db4e3823c1a56b573dbaba67',
    'auth_user': '5907b89c0d3418e90efdaa815d981c84ca554dbcdb470b08ba7c8a6d592d1d4a%3Af9901778bd8ab8ca29c740440719af0502f9456bcbe84fab9c1b88e5d7615344',
    '_ga_QFGG4THJR2': 'GS1.1.1685176601.27.1.1685177344.0.0.0',
    '_ga': 'GA1.1.1443087961.1682255257',
    '_hjSessionUser_3279922': 'eyJpZCI6ImVhYTEwYmIxLWYzMzMtNTVkMi1iZDNhLTgzNDdlNGY0Yzk3NSIsImNyZWF0ZWQiOjE2ODIyNTUyNTc3NjIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.977759639.1684910311',
    'ffmr_thread': '1222216%3A1685034600%2C1222201%3A1685034688%2C1222149%3A1685034625%2C1222326%3A1685034581%2C1217096%3A1685034613%2C1222653%3A1685119023%2C1222659%3A1685119561%2C1222662%3A1685119562%2C1222641%3A1685119564',
    'flexHeight_179': 'undefined',
    'flexHeight_315': 'undefined',
    'flexHeight_155': 'undefined',
    'flexHeight_99': 'undefined',
    'flexHeight_817': 'undefined',
    'flexHeight_992': 'undefined',
    'flexHeight_754': 'undefined',
    '_hjHasCachedUserAttributes': 'true',
    'fftab-history': 'market%2Cindex',
    '__cf_bm': 'x0Qf_StRiJNiXdTmqYadHdB7jO13un0p02sIvazYpRM-1685176602-0-AaO8inMQzT3+7qbdzBlZX73ymEVcEC76W60NWJc2wfQ5X6pQ6vIegfEmffEaD+4ByC0q7eQlrFZaH2TrT0sGHiOFLeUF5vpERkygcsfo2G5nhO0TTWMbCcAtkOVNL6VoECJ31eX5kLdRHU0IIyAPfzIGwUtCsQlyBNjAV15B2mxM',
    '_hjIncludedInSessionSample_3279922': '0',
    '_hjSession_3279922': 'eyJpZCI6IjhlODM4MjUyLWYxMDItNGYzOS1hN2IwLTdjODRjNTQ3NGIxYiIsImNyZWF0ZWQiOjE2ODUxNzY2MDIzOTcsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    '_gat_gtag_UA_3311429_1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/market/eurusd',
    'Connection': 'keep-alive',
    # 'Cookie': 'fflastvisit=1682255256; fflastactivity=0; ffsettingshash=4ba71072db4e3823c1a56b573dbaba67; auth_user=5907b89c0d3418e90efdaa815d981c84ca554dbcdb470b08ba7c8a6d592d1d4a%3Af9901778bd8ab8ca29c740440719af0502f9456bcbe84fab9c1b88e5d7615344; _ga_QFGG4THJR2=GS1.1.1685176601.27.1.1685177344.0.0.0; _ga=GA1.1.1443087961.1682255257; _hjSessionUser_3279922=eyJpZCI6ImVhYTEwYmIxLWYzMzMtNTVkMi1iZDNhLTgzNDdlNGY0Yzk3NSIsImNyZWF0ZWQiOjE2ODIyNTUyNTc3NjIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.977759639.1684910311; ffmr_thread=1222216%3A1685034600%2C1222201%3A1685034688%2C1222149%3A1685034625%2C1222326%3A1685034581%2C1217096%3A1685034613%2C1222653%3A1685119023%2C1222659%3A1685119561%2C1222662%3A1685119562%2C1222641%3A1685119564; flexHeight_179=undefined; flexHeight_315=undefined; flexHeight_155=undefined; flexHeight_99=undefined; flexHeight_817=undefined; flexHeight_992=undefined; flexHeight_754=undefined; _hjHasCachedUserAttributes=true; fftab-history=market%2Cindex; __cf_bm=x0Qf_StRiJNiXdTmqYadHdB7jO13un0p02sIvazYpRM-1685176602-0-AaO8inMQzT3+7qbdzBlZX73ymEVcEC76W60NWJc2wfQ5X6pQ6vIegfEmffEaD+4ByC0q7eQlrFZaH2TrT0sGHiOFLeUF5vpERkygcsfo2G5nhO0TTWMbCcAtkOVNL6VoECJ31eX5kLdRHU0IIyAPfzIGwUtCsQlyBNjAV15B2mxM; _hjIncludedInSessionSample_3279922=0; _hjSession_3279922=eyJpZCI6IjhlODM4MjUyLWYxMDItNGYzOS1hN2IwLTdjODRjNTQ3NGIxYiIsImNyZWF0ZWQiOjE2ODUxNzY2MDIzOTcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gat_gtag_UA_3311429_1=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'limit': '8',
}

response = requests.get('https://www.forexfactory.com/upcoming/EURUSD', params=params, cookies=cookies, headers=headers)


# -----------------------------------------------------------------------------
# News
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/market/eurusd',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'instrument': 'EUR/USD',
    'interval': 'M5',
    'from': '1685074800',
    'to': '1685134500',
}

response = requests.get('https://mds-api.forexfactory.com/indicators/news', params=params, headers=headers)

# -----------------------------------------------------------------------------
# BARS
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/market/eurusd',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'to': '1685074799',
    'interval': 'M5',
    'instrument': 'EUR/USD',
    'per_page': '200',
    'extra_fields': '',
}

response = requests.get('https://mds-api.forexfactory.com/bars', params=params, headers=headers)

# -----------------------------------------------------------------------------
# MARCO
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/market/eurusd',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get(
    'https://mds-api.forexfactory.com/bars/aggregate?requests[]=SPX%2FUSD,12,H1&requests[]=Nikkei225%2FUSD,12,H1&requests[]=FTSE100%2FUSD,12,H1&requests[]=DXY%2FUSD,12,H1&requests[]=WTI%2FUSD,12,H1&requests[]=Gold%2FUSD,12,H1&requests[]=BTC%2FUSD,12,H1&requests[]=VIX%2FUSD,12,H1',
    headers=headers,
)


# -----------------------------------------------------------------------------
# EVENTS
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/market/eurusd',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'instrument': 'EUR/USD',
    'interval': 'H4',
    'from': '1681218000',
    'to': '1685120400',
}

response = requests.get('https://mds-api.forexfactory.com/indicators/news', params=params, headers=headers)