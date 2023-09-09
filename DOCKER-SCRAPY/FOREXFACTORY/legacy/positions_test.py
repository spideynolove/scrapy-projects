from requests import post
from crawldata.functions import *

headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------48222048032047603611657549096'

# params = {
#     'onlyContent': 'true',
#     'section': 'details',
#     # 'currency': 'GBPUSD',
#     'currency': 'EURUSD',
#     'row': '1',
# }

# params = {
#     'more': '2',
# }

# data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][idSuffix]"\r\n\r\n909478547\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][modelData]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="currency"\r\n\r\nEURUSD\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="row"\r\n\r\n0\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][trades/positions/traders/type]"\r\n\r\nentry\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][trades/positions/traders/private][]"\r\n\r\n1\r\n-----------------------------48222048032047603611657549096--\r\n'
# # data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][idSuffix]"\r\n\r\n1355900096\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][modelData]"\r\n\r\n\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="currency"\r\n\r\nUSDCHF\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="row"\r\n\r\n0\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][trades/positions/traders/type]"\r\n\r\nlots\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions/Traders_positionTraders][trades/positions/traders/private][]"\r\n\r\n1\r\n-----------------------------48222048032047603611657549096--\r\n'

params = {
    'onlyContent': 'true',
    'section': 'details',
    'currency': 'USDCHF',
    'row': '0',
}

data = '-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nyes\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][idSuffix]"\r\n\r\nusdchf\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][modelData]"\r\n\r\neyJzaW5nbGVfaW5zdHJ1bWVudCI6IlVTRENIRiIsIl9fZmxleERlZmF1bHRzX18iOnsidHJhZGVzXC9wb3NpdGlvbnNcL3R5cGUiOiJkdWFsIn19\r\n-----------------------------48222048032047603611657549096\r\nContent-Disposition: form-data; name="flex[Trades/Positions_instrumentPositions][trades/positions/type]"\r\n\r\ndual\r\n-----------------------------48222048032047603611657549096--\r\n'

response = post('https://www.forexfactory.com/flex.php', params=params, headers=headers, data=data)
print(response.text)