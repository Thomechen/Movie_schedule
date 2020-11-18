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
request = requests.session()
#套件輸入
title_list = []
title_link_list = []
version_list = []
theater_list = []
theater_list_link = []
#清單建立
i = 1
for i in range(4):
    url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx?p='+str(i)
    r = request.get(url)
    #開起網頁
    soup = BeautifulSoup(r.text,'html.parser')
    title = soup.select('h2 a')
    for t in title:
        title_list.append(t.text)
        title_link_list.append('https://www.vscinemas.com.tw/vsweb/film/'+t.get('href')+'#')

for i in range(1,len(title_list),1):
    print(str(i),'.',title_list[i])
    
select = input('Enter the no:')
url = title_link_list[int(select)]
r = request.get(url)
soup = BeautifulSoup(r.text,'html.parser')
theater = soup.select('p a')
for i in theater:
    theater_list.append(i.text)
    theater_list_link.append((i.get('href'))[1:])
for i in range(len(theater_list)):
    print(str(i)+'.'+theater_list[i])

select = input('Enter the no:')
date = soup.select('article#'+str(theater_list_link[int(select)])+" div.movieDay" )

for d in date:
    print(d.text)