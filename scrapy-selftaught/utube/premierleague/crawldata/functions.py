from datetime import datetime
from pathlib import Path
from sys import path

MIC_PATH = Path(__file__).resolve().parent.parent
PROJECT_PATH = MIC_PATH.parent
NOW = datetime.now()
UNIXTIME = str(datetime.timestamp(NOW)*1000).split('.')[0]
CRAWL_DATE = NOW.strftime('%Y-%m-%d')
LOG_TIME = NOW.strftime('%d%m%Y')

path.append(str(PROJECT_PATH.absolute()))
from helpers import *
headers = dict()
# headers = {
#     'User-Agent': random_user_agent(),
# }

fixturesparams = {
    'comps': '1',
    'compSeasons': '489',
    'page': '0',
    'pageSize': '20',
    'sort': 'desc',
    'statuses': 'C',
    'altIds': 'true',
    'teams': '1',
}