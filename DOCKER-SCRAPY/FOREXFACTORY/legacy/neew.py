from requests import get
from crawldata.functions import *
from json import loads

symbols = (
    'EURUSD', 'AUDUSD', 'NZDUSD', 'USDJPY', 'USDCHF', 'USDCAD', 'GBPUSD',
    'EURAUD', 'EURNZD', 'EURCAD', 'EURCHF', 'EURJPY', 'EURGBP',
    'GBPAUD', 'GBPNZD', 'GBPCAD', 'GBPCHF', 'GBPJPY',

    'XAUUSD',
    'XAGUSD',
    'AUDNZD', 'AUDCAD', 'AUDCHF', 'AUDJPY',
    'NZDCAD', 'NZDCHF', 'NZDJPY',
    'CADCHF', 'CADJPY',
    'CHFJPY',
)

symbols = [symbol.lower() for symbol in symbols]
print(symbols)