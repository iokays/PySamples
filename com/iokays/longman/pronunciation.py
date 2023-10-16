#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os.path

import requests
import requests_cache
import time
import json
from bs4 import BeautifulSoup

def download_mp3(word: str):
    requests_cache.install_cache(backend=requests_cache.SQLiteCache(f'cache/longman_3000.db'))
    url = 'https://www.ldoceonline.com/dictionary/'

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"}

    html = requests.get(url + word, headers=header)

    #保存内容
    html_file_url = 'html/' + word + '.html'
    with open(html_file_url, 'wb') as f:
        f.write(html.content)
        f.close()

    soup = BeautifulSoup(html.text, 'lxml')

    span = soup.find('span', class_='ldoceEntry Entry')

    mp3_url = span.find('span', class_='speaker brefile fas fa-volume-up hideOnAmp').get('data-src-mp3')
    print(mp3_url)

    mp3_file_url = 'html/' + word + '.mp3'

    if not os.path.exists(mp3_file_url):
        mp3 = requests.get(mp3_url, headers=header)
        with open(mp3_file_url, 'wb') as f:
            f.write(mp3.content)
            f.close()
            print('download mp3 success')


# 读取longman_3000.txt文件
# with open('longman_3000.txt', 'r') as f:
#     for line in f.readlines():
#         word = line.strip()
#         print(word)
#         download_mp3(word)
#         time.sleep(1)

# 读取data.json文件
with open('data.json', 'r') as f:
    data = json.load(f).get('words')
    for word in data:
        print(word)
        download_mp3(word.get('word').replace(' ', '-'))
        # time.sleep(1)













