# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:27:02 2021

@author: Mgyu
"""

from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:/Users/Mgyu/Desktop/PL/python/python YT/webscraping/chromedriver.exe")

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기(좌표 입력하는 방식)
#browser.execute_script("window.scrollTo(0, 1080)") # 해상도가1920 x 1080 이기 때문에 세로 1080 설정

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초 간격으로 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수정
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval) # 페이지 로딩 대기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("가장 아래입니다.")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
           ,"Accept-Language":"ko=KR,ko"} # 한글 페이지 요청
res = requests.get(url, headers= headers)
res.raise_for_status()

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 영화 찾기
    origin_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if origin_price:
        origin_price = origin_price.get_text()
    else:
        # print(title,"<이 영화는 할인 하지 않습니다>")
        continue

    # 할인된 가격
    dis_price = movie.find("span", attrs= {"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    # 링크
    link = movie.find("a", attrs= {"class":"JC71ub"})["href"]
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {origin_price}")
    print(f"할인 후 금액 : {dis_price}")
    print("링크: ", "https://play.google.com"+ link)
    print("-" * 30)

browser.quit()