import requests
import re
from bs4 import BeautifulSoup

def html():
    url = 'http://www.quanshuwang.com/?tdsourcetag=s_pcqq_aiomsg'
    req = requests.get(url)
    req.encoding = 'gbk'
    return (req.text)

def urls(aaa):
    r = re.findall(r'<a target="_blank" href="(.*?)"',aaa,re.S)
    for i in r:
        req = requests.get(i)
        req.encoding='gbk'
        aa = req.text
        r=re.findall(r'<div class="b-oper".*?<a href="(.*?)".*?',aa,re.S)[0]
        reqs = requests.get(r)
        reqs.encoding='gbk'
        bb = reqs.text
        res = re.findall(r'<div class="cle.*?<li>.*?<a href="(.*?)"',bb,re.S)

        for i in res:
            reqa = requests.get(i)
            reqa.encoding='gbk'
            cc = reqa.text
            soup = BeautifulSoup(cc,"html.parser")
            a = soup.find('div',class_="mainContenr")
            n= a.text
            with open('xiaoshuo.txt','a',encoding='utf-8') as f:
                f.write(n.replace(u'\xa0', u''))
                print('success')






def main():
    aaa = html()
    a = urls(aaa)


if __name__ == '__main__':
    main()
