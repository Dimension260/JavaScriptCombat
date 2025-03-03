import requests
from lxml import etree
from urllib.parse import urljoin

url ="https://www.shicimingju.com/book/sanguoyanyi.html"

headers = {

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'

}


response = requests.get(url,headers = headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)

name = tree.xpath('//div[@class="contbox cont11"]/div/a/text()')
# print(name)
href = tree.xpath('//div[@class="contbox cont11"]/div/a/@href')
# print(href)
url = 'https://www.shicimingju.com/'

for names,hrefs in zip(name,href):
    full_url = 'https://www.shicimingju.com/' + str(hrefs)

    print(names,full_url)