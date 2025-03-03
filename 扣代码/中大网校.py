import base64
import requests
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# def base64_api(img_base64):
#     data = {"username": "q6035945", "password": "q6035945", "typeid": 1003, "image": img_base64}
#     result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#     return ""
session = requests.Session()
session.headers = {
        'referer':'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F',
        'content-type':'application/json;charset=UTF-8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

def login():
    img_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
    session.headers = {
        'referer':'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F',
        'content-type':'application/json;charset=UTF-8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    img_resp = session.post(img_url,headers=session.headers)
    # print(img_resp.text)
    img_base64 = img_resp.json()['data'].split('base64,')[-1]
    # with open('img_base64.png','wb') as f:
    #     f.write(base64.b64decode(img_base64))
    #     # f.close()
    # verify_code = base64_api(img_base64)
    # print(verify_code)

    # rsa的key
    rsa_public_key_base64= "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
    ress =session.post('https://user.wangxiao.cn/apis//common/getTime',headers=session.headers)
    mypassword = 'Dimension722'
    password = mypassword + '' + ress.json()['data']

    public_key = RSA.importKey(base64.b64decode(rsa_public_key_base64))
    rsa = PKCS1_v1_5.new(public_key)
    mi_password = rsa.encrypt(password.encode('utf-8'))
    mi_password = base64.b64encode(mi_password).decode()
    # print(mi_password)

    data = {
        'imageCaptchaCode': 'verify_code',
        'password': mi_password,
        'userName': "19012719742"
    }

    login_resp = session.post(url = 'https://user.wangxiao.cn/apis//login/passwordLogin',headers=session.headers,data=json.dumps(data,separators=(',',':')))

    # print(login_resp.text)
    # resp = session.post(url="https://user.wangxiao.cn/apis//login/passwordLogin",data=json.dumps(data, separators=(',', ':')),headers=session.headers)

    login_info = login_resp.json()

    session.cookies['autoLogin'] = None
    session.cookies['userInfo'] = json.dumps(login_info['data'],separators=(',',':'))
    session.cookies['token'] = login_info['data']['token']
    login_data = login_info['data']

    session.cookies['UserCookieName'] = login_data['userName']
    session.cookies['OldUsername2'] = login_data['userNameCookies']
    session.cookies['OldUsername'] = login_data['userNameCookies']
    session.cookies['OldPassword'] = login_data['passwordCookies']
    session.cookies['UserCookieName_'] = login_data['userName']
    session.cookies['OldUsername2_'] = login_data['userNameCookies']
    session.cookies['OldUsername_'] = login_data['userNameCookies']
    session.cookies['OldPassword_'] = login_data['passwordCookies']
    session.cookies[login_data['userName'] + "_exam"] = login_data['sign']

def get_info():
    for i in range(3):
        # 测试, 登陆状态是否可用.  <- 跑的多的.
        resp = session.post(url="http://ks.wangxiao.cn/practice/listQuestions",
                     data=json.dumps({
                        "examPointType":"",
                        "practiceType":"2",
                        "questionType":"",
                        "sign":"jz1",
                        "subsign":"8cc80ffb9a4a5c114953",
                        "top":"30",
                    }, separators=(',', ':'))
                    ,headers={
                        "Content-Type": "application/json;charset=UTF-8",
                    })
        # 如果登陆状态可以的话. 可以获取到题目内容
        if resp.text.startswith("{"):
            return resp.json()
        else:
            # 登陆失败. 或者登陆信息失效. 登陆过期
            login()


dta =  get_info()
print(dta)