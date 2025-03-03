import requests
from lxml import etree
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'referer': 'https://movie.douban.com/top250?start=0&filter=',
    'cookie': 'bid=gjAvs15r-48; _ga=GA1.2.275733507.1740293969; _gid=GA1.2.1229840802.1740293969; _ga_Y4GN1R87RG=GS1.1.1740293968.1.0.1740293971.0.0.0; __utma=30149280.275733507.1740293969.1740294031.1740294031.1; __utmb=30149280.0.10.1740294031; __utmc=30149280; __utmz=30149280.1740294031.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0'
}

with open("douban_movies.csv", "w", newline="", encoding="utf_8_sig") as f:  # 打开文件准备写入
    for i in range(0, 10):
        start = i * 25  # 修正分页逻辑，每页25条数据
        url = f"https://movie.douban.com/top250?start={start}"
        response = requests.get(url, headers=headers)
        tree = etree.HTML(response.content.decode('utf-8'))

        # 提取标题的三个部分（注意检查XPath是否与页面结构匹配）
        title1 = tree.xpath('//div[@class="article"]/ol/li/div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
        title2 = tree.xpath('//div[@class="article"]/ol/li/div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[2]/text()')
        title3 = tree.xpath('//div[@class="article"]/ol/li/div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[3]/text()')

        # 将标题组合并写入文件
        for t1, t2, t3 in zip(title1, title2, title3):
            t1_clean = t1.strip()
            t2_clean = t2.strip()
            t3_clean = t3.strip()
            total_title = f"{t1_clean}{t2_clean}{t3_clean}".strip().replace(' ','').replace('/',',')  # 用空格分隔三部分
            writer = csv.writer(f)
            writer.writerows(total_title + '\n')
