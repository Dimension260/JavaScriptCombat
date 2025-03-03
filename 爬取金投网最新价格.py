import requests
from lxml import etree

url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'
headers = {

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'

}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)

title = tree.xpath('//div[@class="det_content"]/table/tbody/tr/td[1]/text()')
# print(title)
price = tree.xpath('//div[@class="det_content"]/table/tbody/tr/td[3]/text()')

for title, price in zip(title, price):
    print(title, price)