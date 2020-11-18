import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
request = requests.session()
i = 1
movie_title_list = []
movie_id_list = []
movie_id_list_1 = []
movie_title_list_cn = []
movie_title_list_en = []
try:
    for i in range(10):
        url = 'https://movies.yahoo.com.tw/movie_intheaters.html?page='+str(i)
        r = request.get(url)
        soup = BeautifulSoup(r.text,'html.parser')
        movie_title = soup.select('div.release_movie_name a')
        for m in movie_title:
            movie_title_list.append(m.text.strip())
            if '-' in m.get('href')[-5]:
                movie_id_list.append(m.get('href')[-4:])
            else:
                movie_id_list.append(m.get('href')[-5:])
except NameError:
    print('頁數已到底')
for m in range(0,len(movie_title_list),2):
    movie_title_list_cn.append(movie_title_list[m])
for m in range(1,len(movie_title_list),2):
    movie_title_list_en.append(movie_title_list[m])
for m in range(1,len(movie_id_list),2):
    movie_id_list_1.append(movie_id_list[m])


for c in range(len(movie_title_list_cn)):
    print(str(c),'-',movie_title_list_cn[c],'-',movie_title_list_en[c])

#目前只抓到電影列表
'''
select = input('Movie_select:')
url = 'https://movies.yahoo.com.tw/movietime_result.html/id='+str(movie_id_list_1[int(select)])
r = request.get(url)
print(r.text)
# soup = BeautifulSoup(r.text,'html.parser')
# theater = soup.select('li.adds a')
# for t in theater:
#     print(t.get('href'))
    


data = {'Movie_title_cn':movie_title_list_cn,'Movie_title_en':movie_title_list_en,'Movie_id':movie_id_list_1}
df = pd.DataFrame(data)
'''