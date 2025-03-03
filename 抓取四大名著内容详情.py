import requests
from lxml import etree

url = 'https://www.shicimingju.com//book/sanguoyanyi/1.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'referer': 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
contents = tree.xpath('//div[@class="contbox textinfor"]/div/p/text()')
for content in contents:
    contents = content.replace('xa0', '').replace('\\','')
    # print(contents)