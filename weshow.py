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
browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(10)
browser.get(url)
locator = (By.CLASS_NAME,'versionFirst')
WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))
soup = BeautifulSoup(browser.page_source,'html.parser')

# version = soup.select('a.versionFirst')
# for v in version:
#     version_list.append(v.text)
# for v in range(len(version_list)):
#     print(str(v),'.',version_list[v])
# select = input('Enter the no:')
# move = browser.find_element_by_link_text(str(version_list[int(select)]))
# locator = (By.CLASS_NAME,'icon-chevron-right')
# WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))

theater = soup.select('p a')
for i in theater:
    theater_list.append(i.text)
for i in range(len(theater_list)):
    print(str(i)+'.'+theater_list[i])
select = input('Enter the no:')
click = browser.find_element_by_link_text(str(theater_list[int(select)])).click()
locator = (By.CLASS_NAME,'seat')
WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))
#以下要進行修正
'''
date = soup.select('article.hidden.article.slide h4')
time = soup.select('article.hidden.article.slide a')
for d in date:
    print(d.text)
    for t in time:
        print(t.text)
browser.quit()
'''