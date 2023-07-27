from requests import get, post
from crawldata.functions import *

# # response = get('https://bongdaplus.vn/tin-moi', headers=headers)
# # print(response.text) 


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
}

data = {
    'objectid': '402729',   # 402725
    'objecttype': '0',
    'fullname': 'Kid magician',
    'email': 'marika16792.gamer@gmail.com',
    'parentid': '0',
    'comment': 'Bán nửa đội hình hiện tại cho thoáng, khắc sẽ có ý tưởng mua thêm ai',
    'reply2to': '',
}

response = post('https://bongdaplus.vn/postcomment/', 
                headers=headers, 
                data=data)

print(response.status_code) 