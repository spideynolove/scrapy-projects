from boltons.iterutils import remap
from datetime import datetime, timezone, timedelta
from dateutil import parser
# from dateparser import parse
from fake_useragent import VERSION, UserAgent
from json import dump, dumps, load, loads
from pathlib import Path
from pydantic.utils import deep_update
from pymongo import MongoClient
from unicodedata import normalize
from urllib.parse import urlencode
from random import randint
from re import sub, findall
from redis import from_url
from requests import get, post

NOW = datetime.now()
UNIXTIME = str(datetime.timestamp(NOW)*1000).split('.')[0]
CRAWL_DATE = NOW.strftime('%Y-%m-%d')
LOG_TIME = NOW.strftime('%d%m%Y')
CURRENT_PATH = Path(__file__).resolve().parent

IGNORES = ['google',]

def random_user_agent():
    # # VERSION==1.1.3
    # ua_loc = f'{CURRENT_PATH}/fake_useragent{VERSION}.json' 
    # ua = UserAgent(use_external_data=True, cache_path=ua_loc)
    ua = UserAgent(min_percentage=1.3)
    return ua.random

def rand_timeout(min: int = 8, max: int = 13) -> int:
    return 100*randint(min, max)

def get_time(days: str = None, isfuzzy: bool = False, divide: int = 1, have_hour: bool=False) -> str:
    hour = ' %H:%M' if have_hour else ''
    return parser.parse(days, fuzzy=isfuzzy).strftime(f'%Y-%m-%d{hour}') if days else ""

def get_unixtime(timestamp: str = None, divide: int = 1000, have_hour: bool=False) -> str:
    hour = ' %H:%M' if have_hour else ''
    return datetime.fromtimestamp(int(timestamp)/divide).strftime(f'%Y-%m-%d{hour}') if timestamp else ""

def get_tztime(delta: int = 0):
    return (datetime.now(timezone.utc) + timedelta(delta)).replace(tzinfo=None).isoformat(timespec="seconds") + 'Z'

def check_dirs(folder: str = None):
    if not Path(folder).exists():
        Path(folder).mkdir(parents=True, exist_ok=True)

def fill_quote(string: str = None, base: str = 'https://www.fxstreet.com/macroeconomics/central-banks/{}') -> str:
    return base.format(string) if string else ""

def get_num(string: str = None,
            filter_:str = r"([^0-9.-])") -> str:
    return sub(filter_, "", str(string).strip()) if string else ""

def checknull(string: str = None) -> str:
    return string if string else ""

def clean_str(string: str = None) -> str:
    return string.replace('“', '').replace('”', '').strip() if string else ""

def clean_lst(lst: list = None) -> list:
    lst = [clean_str(normalize('NFKD', ''.join(item))) for item in lst if 'Also read:' not in ''.join(item)]
    return list(filter(None, lst))

def flatten_lst_dct(lst: list = None):
    return {k: v for d in lst for k, v in d.items()}

def sort_dict(dct: dict = None) -> dict:
    return {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}

def clear_dict(dct: dict = None) -> dict:
    return {k: v for k, v in dct.items() if v}

def lst_to_dict(items: list = None) -> dict:
    # convert list of list to dict
    return {item[0]: item[1] for item in items}

def flatten(l):
    return [item for sublist in l for item in sublist]

def should_abort_request(req):
    if any(item in req.url for item in IGNORES):
        return True
    if req.resource_type in ("image", "media", "other"):
        return True
    # if req.resource_type == "script":
    #     return True
    # if req.resource_type == "xhr":    # need
    #     return True
    # if req.resource_type == "stylesheet": # slow
    #     return True
    # if req.method.lower() == 'post':
    #     # logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
    #     return True
    return False

def get_chunks(lst: list = None, n: int = None) -> list:
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def del_dictkeys(dict_: dict = None, keys: set = None):
    '''  https://stackoverflow.com/questions/3405715/elegant-way-to-remove-fields-from-nested-dictionaries '''
    drop_keys = lambda path, key, value: key not in keys
    return remap(dict_, visit=drop_keys)

def cvtime_dict(dict_: dict = None, key: str = None, func: object = get_time):
    return deep_update(dict_, {key: func(dict_[key], divide=1, have_hour=True)} )