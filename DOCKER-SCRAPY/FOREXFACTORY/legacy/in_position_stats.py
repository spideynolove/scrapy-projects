import requests

cookies = {
    'fflastvisit': '1682255256',
    'fflastactivity': '0',
    'ffsettingshash': '4ba71072db4e3823c1a56b573dbaba67',
    'auth_user': '7372c47658612ae859b7aeb98b77fa0366f0802e5077323c2d1b3cbcb0501995%3A6d29767247a0c625683f3433902e48967370add38533282d43dbefd6465a9be7',
    '_ga_QFGG4THJR2': 'GS1.1.1684935278.14.1.1684937417.0.0.0',
    '_ga': 'GA1.2.1443087961.1682255257',
    '_hjSessionUser_3279922': 'eyJpZCI6ImVhYTEwYmIxLWYzMzMtNTVkMi1iZDNhLTgzNDdlNGY0Yzk3NSIsImNyZWF0ZWQiOjE2ODIyNTUyNTc3NjIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.977759639.1684910311',
    'ffmr_thread': '1222216%3A1684936505%2C1222201%3A1684936521%2C1222149%3A1684937373',
    'flexHeight_179': 'undefined',
    '_hjHasCachedUserAttributes': 'true',
    'flexHeight_315': 'undefined',
    '_hjIncludedInSessionSample_3279922': '0',
    'sessions_live': '1',
    'fftab-history': 'index%2Cnews%2Cmarket%2Ccalendar%2Ctrades',
    'flexHeight_155': 'undefined',
    '__cf_bm': 'LbrPX4LhFTOr8xtD.k0hJ1IEesaiT1ia734nvH2BytU-1684935773-0-AYu0nC/RaZ3StVYKX4Vy7Z5LqGxwytKi93yjbBD9dOqHfgFZZHqAMKWaL8wgOZc5N7h5qswDt+HEc/ExHrESoePnsjOjYhjeOUbgHc9kB+8rp3XNokjjZWndKanwvblsrnNRU7IJQUbT7gWcHFFZ4eihtZ2K1oDeLKCtgbJyZLkH',
    'flexHeight_99': 'undefined',
    '_hjSession_3279922': 'eyJpZCI6Ijk3MmQyY2MxLWRhZjUtNGQ4ZC05ZWExLTJhZTllYmMyYWFlZSIsImNyZWF0ZWQiOjE2ODQ5MzU3NzM0NDUsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'flexHeight_817': 'undefined',
    'ffflextime_flex_news_newsLeft1': '1684937388-0',
    'ffflextime_flex_news_newsLeft2': '1684937383-0',
    'ffflextime_flex_trades/positions_tradesPositionsCopy1': '1684937436-1',
    'flexHeight_992': 'undefined',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.forexfactory.com/',
    'Content-Type': 'multipart/form-data; boundary=---------------------------92931819128168045952659538885',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'fflastvisit=1682255256; fflastactivity=0; ffsettingshash=4ba71072db4e3823c1a56b573dbaba67; auth_user=7372c47658612ae859b7aeb98b77fa0366f0802e5077323c2d1b3cbcb0501995%3A6d29767247a0c625683f3433902e48967370add38533282d43dbefd6465a9be7; _ga_QFGG4THJR2=GS1.1.1684935278.14.1.1684937417.0.0.0; _ga=GA1.2.1443087961.1682255257; _hjSessionUser_3279922=eyJpZCI6ImVhYTEwYmIxLWYzMzMtNTVkMi1iZDNhLTgzNDdlNGY0Yzk3NSIsImNyZWF0ZWQiOjE2ODIyNTUyNTc3NjIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.977759639.1684910311; ffmr_thread=1222216%3A1684936505%2C1222201%3A1684936521%2C1222149%3A1684937373; flexHeight_179=undefined; _hjHasCachedUserAttributes=true; flexHeight_315=undefined; _hjIncludedInSessionSample_3279922=0; sessions_live=1; fftab-history=index%2Cnews%2Cmarket%2Ccalendar%2Ctrades; flexHeight_155=undefined; __cf_bm=LbrPX4LhFTOr8xtD.k0hJ1IEesaiT1ia734nvH2BytU-1684935773-0-AYu0nC/RaZ3StVYKX4Vy7Z5LqGxwytKi93yjbBD9dOqHfgFZZHqAMKWaL8wgOZc5N7h5qswDt+HEc/ExHrESoePnsjOjYhjeOUbgHc9kB+8rp3XNokjjZWndKanwvblsrnNRU7IJQUbT7gWcHFFZ4eihtZ2K1oDeLKCtgbJyZLkH; flexHeight_99=undefined; _hjSession_3279922=eyJpZCI6Ijk3MmQyY2MxLWRhZjUtNGQ4ZC05ZWExLTJhZTllYmMyYWFlZSIsImNyZWF0ZWQiOjE2ODQ5MzU3NzM0NDUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; flexHeight_817=undefined; ffflextime_flex_news_newsLeft1=1684937388-0; ffflextime_flex_news_newsLeft2=1684937383-0; ffflextime_flex_trades/positions_tradesPositionsCopy1=1684937436-1; flexHeight_992=undefined',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'onlyContent': 'true',
    'section': 'details',
    'currency': 'GBPUSD',
    'row': '1',
}

data = '-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="securitytoken"\r\n\r\nguest\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="do"\r\n\r\nsaveoptions\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="setdefault"\r\n\r\nno\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="ignoreinput"\r\n\r\nyes\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][idSuffix]"\r\n\r\n\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][_flexForm_]"\r\n\r\nflexForm\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][modelData]"\r\n\r\neyJpc0hvbWVwYWdlIjp0cnVlLCJwYV9sYXlvdXRfaWQiOiJob21lcGFnZSIsInBhX2NvbXBvbmVudF9pZCI6IlRyYWRlUG9zaXRpb25zX0NvcHkxIiwicGFfY29udHJvbHMiOiJob21lcGFnZXxUcmFkZVBvc2l0aW9uc19Db3B5MSIsInBhX2luamVjdHJldmVyc2UiOmZhbHNlLCJwYV9oYXJkaW5qZWN0aW9uIjpmYWxzZSwicGFfaW5qZWN0YXQiOmZhbHNlfQ==\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][trades/positions/type]"\r\n\r\ntraders\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_0]"\r\n\r\nEURUSD\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_1]"\r\n\r\nGBPUSD\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_2]"\r\n\r\nUSDJPY\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_3]"\r\n\r\nUSDCHF\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_4]"\r\n\r\nUSDCAD\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_5]"\r\n\r\nAUDUSD\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_6]"\r\n\r\nNZDUSD\r\n-----------------------------92931819128168045952659538885\r\nContent-Disposition: form-data; name="flex[Trades/Positions_tradesPositionsCopy1][market/currency_7]"\r\n\r\nGBPJPY\r\n-----------------------------92931819128168045952659538885--\r\n'

response = requests.post('https://www.forexfactory.com/flex.php', params=params, cookies=cookies, headers=headers, data=data)