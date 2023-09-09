from pathlib import Path
from sys import path, exit

MIC_PATH = Path(__file__).resolve().parent.parent
PROJECT_PATH = MIC_PATH.parent
path.append(str(PROJECT_PATH.absolute()))
from helpers import *
check_dirs(f"{PROJECT_PATH}/log/logfile/")

fixparams = {
    'comps': '1',
    'pageSize': '20',
    'sort': 'desc',
    'statuses': 'C',
    'altIds': 'true',
    # change this
    'compSeasons': '489',
    'page': '0',
    'teams': '1',   
}

tblparams = {
    # 'compSeasons': '578',
    'altIds': 'true',
    'detail': '2',
    'FOOTBALL_COMPETITION': '1',
    'live': 'true',
}

def gen_urls(api: str = 'https://footballapi.pulselive.com/football/fixtures?{}', 
             params: dict = fixparams):
    return api.format(urlencode(params))