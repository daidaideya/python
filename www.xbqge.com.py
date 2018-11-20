import requests
import re
from bs4 import BeautifulSoup
import os
def html():
    filename = input("书籍名称： "+ '.txt')
    url = 'http://www.xbqge.com/'
    r = requests.get(url)
    r.encoding = 'gbk'
    req = re.findall('<div class="image">.*?<a href="(.*?)">',r.text,re.S)
    #print(req)
    for i in req:
        urls = requests.get(i)
        urls.encoding = 'gbk'
        zhangjie = re.findall('<dd>.*?<a href="(.*?)">',urls.text,re.S)
        for aa in zhangjie:
            neirong = requests.get(i+aa)
            neirong.encoding = 'gbk'
            # print(neirong.text)
            cc = neirong.text
            soup = BeautifulSoup(cc,"html.parser")
            name = soup.find('div', class_='bookname').h1
            content = soup.find('div', id='content').text
            n = str(name.text) + '\n'+ str(content) + '\n\n'
            with open(filename, 'a',encoding='utf-8') as f:
                f.write(n.replace(u'\xa0', u''))
                print(str(name.text) +'\n' +  "打印成功")



def main():
    html()
if __name__ == '__main__':
    main()