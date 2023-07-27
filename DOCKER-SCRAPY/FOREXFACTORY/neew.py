from requests import get
from crawldata.functions import *
from json import loads

params = {
    'instrument': 'GBP/USD',
    'interval': 'D1',
    'from': '1661374800',
    'to': '1685480400',
}

# Indicator news
response = get('https://mds-api.forexfactory.com/indicators/news', 
               params=params, 
               headers=headers)



# params = {
#     'limit': '8',
# }

# response = get('https://www.forexfactory.com/upcoming/GBPUSD', 
#                params=params, 
#                headers=headers)


# params = {
#     'content': 'positions',
#     'do': 'positions_graph_data',
#     'currency': 'GBPUSD',
#     'interval': 'D1',
#     # 'limit': '5',
#     'limit': '800',
# }

# response = get('https://www.forexfactory.com/explorerapi.php', 
#                params=params, 
#                headers=headers)
data = loads(response.text)
print(data)
# print(len(data.get('positions')))
