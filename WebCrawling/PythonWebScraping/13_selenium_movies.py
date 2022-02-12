# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:36:40 2021

@author: Mgyu
"""

import requests
from bs4 import BeautifulSoup

# 예 - 구글 영화
url = "https://play.google.com/store/movies/top"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
           ,"Accept-Language":"ko=KR,ko"} # 한글 페이지 요청
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
print(len(movies))

# with open("movie.html","w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서 예쁘게 출력
# 최초 로딩할떄 10개만 로딩해서 10개만 불러옴

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)
