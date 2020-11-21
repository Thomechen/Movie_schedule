#%%
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import re
import os
#套件輸入
chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument("--window-size=800,600")

request = requests.session()
i = 1
movie_title_list = []
movie_id_list = []
movie_id_list_1 = []
movie_title_list_cn = []
movie_title_list_en = []
calendar_list = []
theater_name_list = []
theater_id_list = []
while True:
    search_or_not = input('Search or not(y/n):')
    if search_or_not == 'y':
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


        select_c = input('Movie_select:')
        url = 'https://movies.yahoo.com.tw/movietime_result.html/id='+str(movie_id_list_1[int(select_c)])
        r = request.get(url)
        soup = BeautifulSoup(r.text,'html.parser')
        calendar = soup.select('label.picker_label h3')
        for c in calendar:
            calendar_list.append(c.text)
        for c in range(len(calendar_list)):
            print(str(c)+'.'+calendar_list[c])

        select_c = input('Date_select:')
        browser = webdriver.Chrome('F:\Python\Movie_schedule\chromedriver.exe')
        browser.implicitly_wait(10)
        browser.get(url)
        locator = (By.CLASS_NAME,'picker_label')
        WebDriverWait(browser,5).until(EC.presence_of_element_located(locator))#等待網頁網取
        select = Select(browser.find_element_by_class_name('moviearea.timelist_area')).select_by_visible_text('台北市')
        click = browser.find_elements_by_class_name('picker_label')[int(select_c)].click()
        sleep(1)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        theater = soup.select('ul.area_time._c.jq_area_time')
        for t in theater:
            theater_name_list.append(t.get('data-theater_name'))
            theater_id_list.append(t.get('id'))#get theater id
        for a in range(len(theater_name_list)):
            print(str(a)+'.'+theater_name_list[a])

        select_c = input('Theater select:')
        time = soup.select('ul#'+str(theater_id_list[int(select_c)])+' input.gabtn') #根據theater id取得時間
        for t in time:
            print(t.get('data-movie_time'))
        browser.quit()
    elif search_or_not == 'n':
        break

    


# %%

# %%
