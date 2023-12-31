#!/bin/pthon
# -*- coding: UTF-8 -*-

###云主机: python3  smth_spider.py
import os
import sys
import json
import random
import re
import time
import urllib.request

from bs4 import BeautifulSoup

API = "https://m.newsmth.net"
def spider(page=1):
    api = "https://m.newsmth.net/board/AutoWorld?p=" +str(page)
    blogcontent = urllib.request.urlopen(api).read()
    soup = BeautifulSoup(blogcontent, 'html.parser')
    #print(soup.prettify())
    title = soup.title.text
    # print(soup.li)
    for items in soup.find_all('li'):
        #print(items)
        dt = items.find_all('div')[1]
        dt = dt.get_text()
        #for div in items.find_all('div'):
        #   print(div)
        # print(items.div.a.attrs['href'])
        title_cmt = items.div.get_text()
        link = items.div.a.attrs['href']
        link = API + link
        title = items.div.a.get_text()
        # 提取互动行为数
        match_obj = re.search(r'.*\((.*?)\).*', title_cmt)
        num = 0
        if match_obj:
           num = match_obj.group(1)

        print("\t".join([title, str(num), link, dt]))
        # break


if __name__ == "__main__":
    for i in range(1, 4928):
    #for i in range(1, 4):
        print("page = ", i)
        try:
            spider(i)
        except:
            pass
        time.sleep(random.randint(2,3))
