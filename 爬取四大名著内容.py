import os
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_html(url):
    # response = requests.get(url, headers=headers)
    # tree = etree.HTML(response.content.decode('utf-8'))
    # return tree
    response = requests.get(url, headers=headers)
    data = response.content.decode()
    # 创建tree对象
    tree = etree.HTML(data)
    return tree


def get_name_href(tree):
    # 抓取四大名著的书名 和 URL

    book_name = tree.xpath('//div[@class="list clear theme2 theme3"]/a/p/text()')
    href = tree.xpath('//div[@class="list clear theme2 theme3"]/a/@href')
    # print(book_name)
    book_name_dict = {}
    for book_name, href in zip(book_name, href):
        artical_url = 'https://www.shicimingju.com/' + href
        bookname = book_name
        book_name_dict[bookname] = artical_url
        # print(bookname + artical_url)
        """  结果如下
        《三国演义》https://www.shicimingju.com//book/sanguoyanyi.html
        《水浒传》https://www.shicimingju.com//book/shuihuzhuan.html
        《西游记》https://www.shicimingju.com//book/xiyouji.html
        《红楼梦》https://www.shicimingju.com//book/hongloumeng.html
        """
    # print(book_name_dict)
    # print(book_name_dict['《三国演义》'])
    return book_name_dict


def get_book_mulu(tree):
    # response = requests.get(book_name_dict['三国演义'], headers=headers)
    # tree_artical = etree.HTML(response.content.decode('utf-8'))
    artical_name = tree.xpath('//div[@class="list"]/a/text()')
    artical_href = tree.xpath('//div[@class="list"]/a/@href')
    # print(artical_href)

    artical = {}
    for artical_href, artical_name in zip(artical_href, artical_name):
        artical_url = 'https://www.shicimingju.com/' + artical_href
        # artical_name_href = artical_url + ' ' + artical_name
        artical[artical_name] = artical_url
        # print(artical_name_href)
    # print(artical)
    return artical


def get_content(tree):
    contents = tree.xpath('//div[@class="contbox textinfor"]/div/p/text()')
    for content in contents:
        # contents = content.replace('xa0', '').replace('\\', '')
        # print(contents)
        return content


def save_book(book_name, mulu_name, contents):
    if not os.path.exists(book_name):
        os.makedirs(book_name)

    with open(os.path.join(book_name, mulu_name + '.txt'), 'w', encoding='UTF-8') as f:
        f.write(contents)


def main(url, headers):
    get_html(url)
    index_tree = get_html(url)
    get_name_href(index_tree)
    for book_name, book_url in get_name_href(index_tree).items():
        mulu_tree = get_html(book_url)
        get_book_mulu(mulu_tree)
        for mulu_name, mulu_url in get_book_mulu(mulu_tree).items():
            mulu_tree = get_html(mulu_url)
            contents = get_content(mulu_tree)
            save_book(book_name, mulu_name, contents)
            # get_content(mulu_tree)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(100)
    url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'referer': 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    }

    # main(url, headers)
    pool.submit(main, url, headers)
    pool.shutdown()
