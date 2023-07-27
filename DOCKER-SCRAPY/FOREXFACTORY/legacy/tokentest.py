
import requests
from crawldata.functions import *

params = {
    'symbols': 'DXY0,^EURUSD,^USDCAD,^USDJPY,^USDCHF,^GBPUSD,^AUDUSD,^USDCNY,^XAUUSD,^XAGUSD',
    'fields': 'symbol,symbolName,symbolType,lastPrice,priceChange,highPrice,lowPrice,tradeTime,hasOptions,symbolCode',
    'meta': 'field.shortName,field.type,field.description',
    'page': '1',
    'raw': '1',
}

cookies, headers = bypass_proxies(headers=headers)

response = requests.get(
    'https://www.barchart.com/proxies/core-api/v1/quotes/get',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)