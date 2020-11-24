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
movie_list = []
movie_link_list = []
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
request = requests.session()
url = 'https://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx?cinema=1|TP'
r = request.get(url,headers = my_headers)
soup = BeautifulSoup(r.text,'html.parser')
title = soup.select('ul.movieList a')

for t in title:
    movie_list.append(t.text)
    movie_link_list.append(t.get('href'))
for t in range(len(movie_list)):
    print(str(t)+'.'+movie_list[t])

select = input('Movie select:')
url = 'https://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx'+movie_link_list[int(select)]
r = request.get(url,headers = my_headers)
soup = BeautifulSoup(r.text,'html.parser')
for t in soup.select('div.movieDay'):
    print(t.text)




# %%
