#%%
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
version_list = []
theater_list = []
theater_list_link = []
date_list = []
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
theater = soup.select('p a')
version = theater.find_parents('a')
'''
for i in theater:
    theater_list.append(i.text)
    theater_list_link.append((i.get('href'))[1:])
for i in range(len(theater_list)):
    print(str(i)+'.'+theater_list[i])
'''
for v in version:
    version_list.append(v.text)
    print(v.text)

'''
select = input('Select Theater:')
print('----------------------------------------------------------------------------------')
select_theater = theater_list[int(select)]#戲院名稱
theater_select = str(theater_list_link[int(select)])
date = soup.select('article#'+str(theater_list_link[int(select)])+" div.movieDay" )

print(' ')
print(select_movie)
print(select_theater)
print(" ")
for d in date:
    print(d.text.strip())
    print('----------------------------------------------------------------------------------')
'''
# %%
