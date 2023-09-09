import requests

cookies = {
    'fflastvisit': '1691742160',
    'fflastactivity': '0',
    'ffsettingshash': 'a5a5ea02f7ab96685a05adce4c797e2b',
    'fftab-history': 'calendar',
    'auth_user': 'd6801a858699fc34f05fc6fe563674bdb1292266c03611ec0babb3d34bfe4883%3A0b0c00b6693a8e108c789ccb8db04698d721235436f65ef3e12bc39daa732bcd',
    '__cf_bm': 'l3PNi8m2c6sCmTyt8fiL6xGMSpz4ApCqM8OEkq3yV.Q-1691742160-0-AdfwT0m9hu5x6sgDiMSKe1bH54YK33/cAFZyW/0rgVNoDrUMaPDbFr3iDu4dXb9az2+Ulko6Y7Wof144mLRLHuTLSUhDtL+A7hXn3ZaHpnFs',
    'cf_clearance': 'WP55oYgl90Yb__3VYYbFIkghlxcqgM5JdQ6i0o3c0E8-1691742161-0-1-448bbbb0.fc1fbd95.138ae450-0.2.1691742161',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.forexfactory.com/calendar',
    'Content-Type': 'application/json',
    'Origin': 'https://www.forexfactory.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
}

params = {
    'navigation': '0',
}

json_data = {
    'begin_date': '2023-08-13',
    'end_date': '2023-08-19',
    'default_view': 'this_week',
    'impacts': [
        3,
        2,
    ],
    'event_types': [
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        10,
        11,
    ],
    'currencies': [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ],
}

response = requests.post(
    'https://www.forexfactory.com/calendar/apply-settings/1',
    params=params,
    # cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)