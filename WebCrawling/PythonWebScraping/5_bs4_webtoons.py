# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 01:36:35 2021

@author: 박민규
"""

import requests
from bs4 import BeautifulSoup

#예 - 네이버 웹툰
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 작품명 가져오기
webtoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 "a" element 출력
for webtoon in webtoons:
    print(webtoon.get_text())


#%%
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=747269&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 가장 위의 웹툰 이름과 해당 링크 가져오기
webtoon_dokja = soup.find_all("td", attrs={"class":"title"})
title = webtoon_dokja[0].a.get_text()
link = webtoon_dokja[0].a["href"]
print(title)
print("연결링크 : https://comic.naver.com"+link)

# 웹툰 회차별 제목 및 해당 링크 가져오기
for dokja in webtoon_dokja:
    title = dokja.a.get_text()
    link =" https://comic.naver.com"+dokja.a["href"]
    print(title, link)

# 회차별 평점 총점, 평균 구하기
total_rates = 0
webtoon_rates = soup.find_all("div", attrs={"class":"rating_type"})
for rate in webtoon_rates:
    dokja_rate = rate.find("strong").get_text()
    print(dokja_rate)
    total_rates += float(dokja_rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates/ len(webtoon_rates))












