import requests        #导入requests包
from bs4 import BeautifulSoup





url = 'http://meowmeow.com.cn/'


def get():
    # print(url)
    res = requests.get(url)
    # print(res.text)
    soup = BeautifulSoup(res.text)
    data = soup.select('.b2_gap > .post-3-li > .item-in > .post-info > h2 > a')
    for item in data:
        print(item.get_text())

get()