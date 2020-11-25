import requests
import pandas as pd
from bs4 import BeautifulSoup
movie_list = []
movie_link_list = []
date_list = []
#清單建立
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
request = requests.session()
url = 'https://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx?cinema=1|TP'
r = request.get(url,headers = my_headers)
soup = BeautifulSoup(r.text,'html.parser')
title = soup.select('ul.movieList a')
#網頁解析
while True:
    s = input('Start(Y/N):')
    if str.upper(s) == 'N':
        break
    elif str.upper(s) == 'Y':
        for t in title:
            movie_list.append(t.text) #電影名稱
            movie_link_list.append(t.get('href')) #電影連結
        for t in range(len(movie_list)):
            print(str(t)+'.'+movie_list[t])
        select = input('Movie select(Quit:n):') #電影選擇
        if str.upper(select) == 'N':
            break
        else:
            print(movie_list[int(select)])
            url = 'https://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx'+movie_link_list[int(select)]
            r = request.get(url,headers = my_headers)
            soup = BeautifulSoup(r.text,'html.parser')
            date = soup.select('div.movieDay')
            #網頁解析
            for t in date:
                date_list.append(t.select('h4')[0].text) #上映日期
            for t in range(len(date_list)):
                print(str(t)+'.'+date_list[t])
            select = input('Date select(Quit:n):')
            if str.upper(select) == 'N':
                break
            else: 
                print(date_list[int(select)])
                str = date_list[int(select)]
                for t in date:
                    if str == t.select('h4')[0].text:
                        for i in t.select('li a'):
                            print(i.text) #上映時間



