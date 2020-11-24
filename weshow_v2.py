#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup
movie_list = []
movie_link_list = []
date_list = []
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
date = soup.select('div.movieDay')
for t in date:
    print(t.text)
    #date_list.append(t.select('h4')[0].text)

'''
select = input('Date select:')
str = date_list[int(select)]
time = soup.find_all('div',{'class':'movieDay'},string = str )
for t in time:
    print(t.select('li'))
'''



# %%
