from crawldata.functions import *

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://www.premierleague.com',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.premierleague.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
#     'DNT': '1',
#     'Sec-GPC': '1',
# }

# # table -----------------------------------------------------------
# params = {
#     'compSeasons': '578',
#     'altIds': 'true',
#     'detail': '2',
#     'FOOTBALL_COMPETITION': '1',
#     'live': 'true',
# }
# url = 'https://footballapi.pulselive.com/football/standings'
# # -----------------------------------------------------------
# params = {
#     'page': '0',
#     'pageSize': '100',
# }
# url = 'https://footballapi.pulselive.com/football/competitions/1/compseasons'
# # -----------------------------------------------------------

# response = get(url, params=params, headers=headers)
# data = loads(response.text)
# print(data)

# with open(f'{MIC_PATH}/clubs.json') as data:
#     parsed_json = load(data)
# # for item in parsed_json:
# #     print(item.get('team').get('name'), item.get('team').get('id'))
# ids = [item.get('team').get('id') for item in parsed_json]
# print(ids)

gen_urls(fixed=fixparams)