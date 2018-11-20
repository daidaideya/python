# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re


def html():
    url = 'http://www.biquge.com.tw/19_19216/'
    req = requests.get(url)
    req.encoding = 'utf-8'
    return (req.text)

def xiaoshuozhangjie(htmls):
    r = re.findall('</a></dd><dd><a href="(.*?)">',htmls,re.S)
    return (r)

def get_html(nr):
    req = requests.get(nr)
    req.encoding = 'gbk'
    reponse = req.text
    soup = BeautifulSoup(reponse, 'html.parser')
    title = soup.find("div", class_="bookname").h1.string

    n = soup.find("div", id="content").text
    path = 'D:/'+ '龙王传说' + '.txt'
    with open(path, 'a') as f:
        f.write('\n\n'+ title.replace(u'\xa0', u'')+'\n\n')
        print(title + "打印成功")
        f.write(n.replace(u'\xa0', u''))





if __name__ == '__main__':
    htmls = html()
    list = xiaoshuozhangjie(htmls)
    for i in list:
        nr = ('http://www.biquge.com.tw' + i)
        get_html(nr)