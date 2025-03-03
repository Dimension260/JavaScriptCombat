# sessionId=1740537667868; Hm_lvt_86efc728d941baa56ce968a5ad7bae5f=1740537667; Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f=1740537667; HMACCOUNT=1BFE2F5825761F77; _bl_uid=aamn27X0lgnbyL6ntrphjLacL1tp
# sessionId=1740537667868; Hm_lvt_86efc728d941baa56ce968a5ad7bae5f=1740537667; Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f=1740537667; HMACCOUNT=1BFE2F5825761F77; _bl_uid=aamn27X0lgnbyL6ntrphjLacL1tp

import requests
import json
import base64
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.PublicKey import RSA

session = requests.session()

session.headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}


session.get('https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F')

# print(session.cookies)

img_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
img_resp = session.post(img_url,headers={
    'content-type':'application/json;charset=UTF-8',
    'content-type':'application/json;charset=UTF-8',
    'referer':'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F'
})

img_base64 = img_resp.json()['data'].split('base64,')[-1]
# print(img_base64)

with open('tu.png', 'wb') as f:
    f.write(base64.b64decode(img_base64))


rsa_pub_key_base64 = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
ress = session.post('https://user.wangxiao.cn/apis//common/getTime',headers={
    'content-type':'application/json;charset=UTF-8',
    'content-type':'application/json;charset=UTF-8',
    'referer':'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F'
})
password = '123456'
password_ming = password + ress.json()['data']

pub_key = RSA.importKey(base64.b64decode(rsa_pub_key_base64))
rsa = PKCS1_OAEP.new(pub_key)
mi_password = rsa.encrypt(password_ming.encode('utf-8'))
mi_password_base64 = base64.b64encode(mi_password).decode()
# print(mi_password_base64)

data = {
    'userName': 'hjkahgfoilk',
    'password': mi_password_base64,
    'imageCaptchaCode': 'imgCode',
}

login_resp = session.post('https://user.wangxiao.cn/apis//login/passwordLogin',data=json.dumps(data,separators=(',', ':')),
headers={
    'content-type':'application/json;charset=UTF-8',
    'content-type':'application/json;charset=UTF-8',
    'referer':'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F'
})

# print(login_resp.text)