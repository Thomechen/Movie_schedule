#%%
import requests
import urllib.request
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import re
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
request = requests.session()
#套件輸入
title_list = []
title_link_list = []
theater_id_list = []
#清單建立
i = 1
for i in range(4):
    url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx?p='+str(i)
    r = request.get(url,headers = my_headers)
    #開起網頁
    soup = BeautifulSoup(r.text,'html.parser')
    title = soup.select('h2 a')
    for t in title:
        title_list.append(t.text)
        title_link_list.append('https://www.vscinemas.com.tw/vsweb/film/'+t.get('href')+'#')

for i in range(1,len(title_list),1):
    print(str(i),'.',title_list[i])
    
select = input('Select Movie:')
print('----------------------------------------------------------------------------------')
select_movie = title_list[int(select)]#電影名稱
url = title_link_list[int(select)]
r = request.get(url,headers = my_headers)
soup = BeautifulSoup(r.text,'html.parser')
theater_id = soup.select('li.show ul p a')
for t in theater_id:
    th_id = t.get('href')
    print(th_id[1:])



# %%
