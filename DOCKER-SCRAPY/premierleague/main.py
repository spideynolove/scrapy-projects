from requests import get, post
from crawldata.functions import *
from json import loads

'''

# cookies = {
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jun+15+2023+11%3A40%3A39+GMT%2B0700+(Indochina+Time)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=14dad99b-74ab-4b77-9e2e-33f2121f2617&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=VN%3BHN&AwaitingReconsent=false',
#     'OptanonAlertBoxClosed': '2023-06-15T04:38:38.844Z',
#     '_ga_844XQSF4K8': 'GS1.1.1686803919.1.1.1686804039.10.0.0',
#     '_ga': 'GA1.2.1689508749.1686803919',
#     '_gid': 'GA1.2.1289858514.1686803919',
#     'datadome': '1wnJVZlvRr7zPYljl2LEFyhuHaG1612wk~0sQcI4FrB-gn40DlcvLVMOtMTOqrUSbL~RL_S7Q0VwZXRY4ja6pfeFsO5FBVbPVgDd7u53SJCZsi51zwuRWixrYu2~OWld',
#     '_dc_gtm_UA-33785302-1': '1',
#     'pl_profile': 'eyJzIjogIld6RXNOelV4TWpNeU1ERmQ6MXE5ZW1mOnJOczZFNVhveTdJRGpiTXJrTWZINUFFYVlnOXh4T3A0UHFWd01aZkN0cVUiLCAidSI6IHsiaWQiOiA3NTEyMzIwMSwgImZuIjogIkh1bmciLCAibG4iOiAiTmd1eWVuIiwgImZjIjogbnVsbH19',
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-site',
#     'Sec-Fetch-User': '?1',
# }

response = get('https://www.premierleague.com/home',
               # cookies=cookies,
               #    headers=headers
               )

# print(response.status_code)
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Origin': 'https://www.premierleague.com',
}

params = {
    'comps': '1',
    'compSeasons': '489',
    'page': '0',
    'pageSize': '20',
    'sort': 'desc',
    'statuses': 'C',
    'altIds': 'true',
    'teams': '1',
}

response = get('https://footballapi.pulselive.com/football/fixtures',
               params=params,
               headers=headers
               )

data = loads(response.text)
print(data)