from hashlib import md5
import requests
import time

url = 'https://dict.youdao.com/webtranslate'

tm = str(int(time.time()*1000))

str_temp = f'client=fanyideskweb&mysticTime={tm}&product=webfanyi&key=asdjnjfenknafdfsdfsd'
obj = md5()
obj.update(str_temp.encode('utf-8'))
sign = obj.hexdigest()

word = input('请输入一个单词：')
data = {
    'i': word,
    'from': 'auto',
    'to': '',
    'useTerm': 'false',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': tm,
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg'
}

headers = {
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'zh-CN,zh;q=0.9',
    'connection':'keep-alive',
    'content-length':'329',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'OUTFOX_SEARCH_USER_ID_NCOO=447341850.53694475; OUTFOX_SEARCH_USER_ID=1306502446@115.200.134.6; _uetsid=0f9d6200f7bf11efbb18b3d28dab6211; _uetvid=35d66bf0f10111efa3bbf13a74038a4a; DICT_DOCTRANS_SESSION_ID=OWU2NGMyYmQtYWIyMi00MGYwLWEwNzYtNzM4NWEzZWM5ZGIw',
    'host':'dict.youdao.com',
    'origin':'https://fanyi.youdao.com',
    'referer':'https://fanyi.youdao.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-site',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36}'}
session = requests.session()
resp = session.post(url=url, data=data, headers=headers)
print(resp.text)