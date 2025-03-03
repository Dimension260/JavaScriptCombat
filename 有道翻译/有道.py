import requests
import time
from hashlib import md5


a = int(time.time()*1000)
obj = md5()
obj.update(f'client=fanyideskweb&mysticTime=${a}&product=webfanyi&key=asdjnjfenknafdfsdfsd'.encode('utf-8'))
sign = obj.hexdigest()
# print(sign)

url = 'https://dict.youdao.com/webtranslate'
headers = {
    'referer':'https://fanyi.youdao.com/',
    'cookie':'OUTFOX_SEARCH_USER_ID_NCOO=447341850.53694475; OUTFOX_SEARCH_USER_ID=1306502446@115.200.134.6; _uetsid=35d68570f10111efbc372352773fb516; _uetvid=35d66bf0f10111efa3bbf13a74038a4a; DICT_DOCTRANS_SESSION_ID=ZmY3NzVmODItMTEzZi00YWUxLTkwNDUtOTU2NzRlOTg1OTJk',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}



data = {
    'i': 'like',
    'from': 'auto',
    'to': '',
    'useTerm': 'false',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': a,
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

resopnse = requests.post(url, headers=headers, data=data)
print(resopnse.text)