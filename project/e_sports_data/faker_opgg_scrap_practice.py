# -*- coding: utf-8 -*-
"""Faker_OPGG_scrap practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1TcMLN4ZB7GgvHc8RTd_9ea2mcWGTev
"""

!pip install selenium

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# step1
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium

# step2
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#step3
driver = webdriver.Chrome('chromedriver',options=options)

# 우리가 데이터를 가져올 웹 페이지입니다.
my_opgg_url = 'https://www.op.gg/summoner/userName=midplayer%20or%20AFK'

# selenium이 제어할 chrome을 실행합니다.
#driver = webdriver.Chrome("/Users/namshin/chromedriver")
# driver = webdriver.Chrome("/Users/namshin/chromedriver", options= options)

# 데이터를 가져올 페이지로 이동합니다.
driver.get(my_opgg_url)

#queue_select = Select(driver.find_element_by_css_selector('select.SelectMatchTypes'))

#queue_select.select_by_value('aram')

# '더 보기' 버튼이 활성화되어있으면(리스트의 끝까지 도달하지 않았으면) 계속 클릭하여 이전 게임을 모두 로딩합니다.
while True:
    try:
        driver.find_element_by_css_selector('.GameMoreButton').click()
        # 게임 로딩, html 코드 변경까지 여유 시간을 1초 가집니다.
        time.sleep(1)
        
    # 에러가 나면(페이지에서 '더 보기' 버튼이 없을 경우) while문을 탈출합니다.
    except Exception as e:
        pass
        break

# 결과가 들어갈 빈 리스트를 만듭니다.
my_gametime= []
my_champions = []
my_level = []

# 각 게임에 대해 웹 페이지에 기재된 스탯을 찾아서(selector 사용) 결과 리스트에 append하기
for gamelist in driver.find_elements_by_css_selector('div.GameItemList'):
    for game in gamelist.find_elements_by_css_selector('div.GameItemWrap'):
        my_gametime.append(game.find_element_by_css_selector('div.GameStats').
                           find_element_by_css_selector('div.GameLength').text.strip())
        my_champions.append(game.find_element_by_css_selector('div.ChampionName').text.strip())
        my_level.append(game.find_element_by_css_selector('div.Stats').
                           find_element_by_css_selector('div.Level').text.strip())

# selenium이 제어하는 크롬을 종료합니다.
driver.quit()

len(my_gametime)

# DataFrame으로 변환 후 출력
my_total_df = pd.DataFrame([my_gametime,
                               my_champions,
                                my_level],
                               index = ['gametime','champion','level']).T
my_total_df