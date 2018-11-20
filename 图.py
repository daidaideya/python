# -*- coding:utf-8 -*-
import requests
import re
import os
def html(number):
        url = 'https://alpha.wallhaven.cc/toplist?page=' + str(number)
        req = requests.get(url)
        return (req.text)

def tupian(htmls):
    r = re.findall('<a class="preview" href="(.*?)".*?>',htmls,re.S)
    try:
        for i in r:
            req = requests.get(i)
            #print(resposne.text)
            reqs = req.text
            reqa = re.findall(r'<img id="wallpaper" src="(.*?)".*?>',reqs,re.S)
            html = ('http:' + reqa[0])
            print(html)
            response = requests.get(html)
            filename ='D:/' + 'wallpaper/'+ html[-20:]
            print(filename)
            if not os.path.exists(filename):
                with open(filename, 'wb') as f:
                    f.write(response.content)
                    f.close()
                    print('save picture success')
    except IndexError:
        pass



def main():
    for i in range(1,151):
        htmls = html(i)
        tupian(htmls)

if __name__ == '__main__':
    main()