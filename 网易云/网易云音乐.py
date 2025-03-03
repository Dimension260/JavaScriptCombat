import requests
import execjs

from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen,encoding ='utf-8')



url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=5fa31403a3f6ee03258f6744efc2dc47'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

data = {
    'csrf_token':  "5fa31403a3f6ee03258f6744efc2dc47",
    'encodeType': "aac",
    'ids': "[1325905146]",
    'level': "standard"
    }


f = open ('网易云（第二次）.js','r',encoding= 'utf-8')
js_code = f.read()
f.close()

js = execjs.compile(js_code)
mi = js.call('fn',data)

resp = requests.post(url,headers=headers,data={
    'csrf_token':  "",
    'params' : mi["encText"],
    'encSecKey' : mi['encSecKey']
})
# print(resp.text)
song_url = resp.json()["data"][0]["url"]
# print(song_url)

resp_song = requests.get(song_url,headers=headers)

with open('song.m4a','wb') as f:
    f.write(resp_song.content)