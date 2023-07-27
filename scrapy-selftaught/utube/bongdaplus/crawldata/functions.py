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
headers = {
    'User-Agent': random_user_agent(),
}

FORBIDDEN = ('esports', 'tennis', 'futsal', 'soi-keo', 'emagazine', 'longform')

comdata = {
    # 'objectid': '402723',   # 402725
    'objecttype': '0',
    'fullname': 'Kid magician',
    'email': 'marika16792.gamer@gmail.com',
    'parentid': '0',
    # 'comment': 'Real như hổ mọc thêm cánh',
    'reply2to': '',
}