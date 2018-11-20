import requests

headers ={'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

url = 'https://www.zhihu.com/'

rq = requests.get(url, headers=headers)
print(rq)