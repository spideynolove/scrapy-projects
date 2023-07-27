from requests import Session
from pathlib import Path
from datetime import datetime
from sys import path

SITE_PATH = Path(__file__).resolve().parent.parent
PROJECT_PATH = SITE_PATH.parent
NOW = datetime.now()

CRAWL_DATE = NOW.strftime('%Y-%m-%d %H:%M')
# CRAWL_TIME = NOW.strftime('%H:%M')
LOG_TIME = NOW.strftime('%d%m%Y')
USE_LOCAL_MONGO = True
# TIME_ = CRAWL_DATE + " " + CRAWL_TIME

# accept intervals: H4
CHG_PERIODS = {
    '48hr': ('2,D1', '12,H4', '48,H1'),
    '24hr': ('6,H4', '24,H1'),
    '12hr': ('3,H4', '12,H1'),
    '6hr': ('6,H1',),
    # '5hr': ('5,H1',),
    # '4hr': ('4,H1'),
    # '3hr': ('3,H1',),
    # '2hr': ('2,H1',),
    # '1hr': ('1,H1',),
}
INTERVALS = (
    # 'M5', 
    'H1', 'H4', 
    'D1', 'MN1'
)

QUOTECHECK = ('JPY',)

TEST_SYMBOLS = (
    # 'GBPAUD', 'GBPNZD', 'GBPCAD', 'GBPCHF', 'GBPJPY',
    'USDJPY',
    # 'USDCAD',
)

BB_PERIODS = ('M5', 'H1', 'D1')
SYMBOLS = (
    'EURUSD',
    'AUDUSD', 'NZDUSD', 'USDJPY', 'USDCHF', 'USDCAD', 'GBPUSD',
    'EURAUD', 'EURNZD', 'EURCAD', 'EURCHF', 'EURJPY', 'EURGBP',
    'GBPAUD', 'GBPNZD', 'GBPCAD', 'GBPCHF', 'GBPJPY',

    # 'XAUUSD',
    # 'XAGUSD',
    # 'AUDNZD', 'AUDCAD', 'AUDCHF', 'AUDJPY',
    # 'NZDCAD', 'NZDCHF', 'NZDJPY',
    # 'CADCHF', 'CADJPY',
    # 'CHFJPY',
)

MACROSYMBOLS = (
    'SPXUSD', 'Nikkei225USD','FTSE100USD', 'DXYUSD', 'WTIUSD', 
    'GoldUSD', 'BTCUSD', 'VIXUSD'
)

path.append(str(PROJECT_PATH.absolute()))
from helpers import *
headers = {
    'User-Agent': random_user_agent(),
}

IGNORES = (
    'ads',
    # 'everesttech',
    # 'smartadserver',
    # 'google',
    # 'cloudfront',
)

def should_abort_request(req):
    if any(item in req.url for item in IGNORES):
        return True

    if req.resource_type == "image":
        return True

    if req.resource_type == "media":
        return True

    # if req.resource_type == "script":
    #     return True

    # if req.resource_type == "xhr":    # need
    #     return True

    # if req.resource_type == "stylesheet": # slow
    #     return True

    # if req.resource_type == "other":
    #     return True

    # if req.method.lower() == 'post':
    #     # logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
    #     return True

    return False


def get_unix(time_: datetime = None, multiply: int = 1000):
    return str(datetime.timestamp(time_)*multiply).split('.')[0]


def get_number(string: str = None, rnum: int=4) -> str:
    string = get_num(string)
    return str(round(float(string), rnum)) if string else ''

def gen_perform(symbols: tuple = None, periods: tuple = None):
    symbols = [symbol[:3] + '%2F' + symbol[3:] for symbol in symbols]
    RETS = [list(zip([symbol]*len(period), period)) for symbol in symbols for period in periods.values()]
    return (','.join(item) for item in flatten(RETS))

def revert_perform(string: str = None):
    string = string.split(',')
    return string[0].replace('%2F', ''), ''.join(string[1:])