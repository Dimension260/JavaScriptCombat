import requests
from lxml import etree
from urllib.parse import urljoin

url = 'https://app.mi.com/catTopList/0?page=1'
headers = {
    'referer':'https://app.mi.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

resp = requests.get(url,headers = headers)
data = etree.HTML(resp.content.decode())

name = data.xpath('//div[@class="applist-wrap"]/ul[@class="applist"]/li/h5/a/text()')
url = data.xpath('//div[@class="applist-wrap"]/ul[@class="applist"]/li/h5/a/@href')
for url in url:
    # urls = url.join('https://app.mi.com',url)
    print(url)