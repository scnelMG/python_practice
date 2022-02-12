# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:52:09 2022

@author: Mgyu
"""

# Quiz) 부동산 매물 정보를 스크래핑하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ========== 매물 1 ===========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23

# [주의 사항]
# -실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

import requests
from bs4 import BeautifulSoup

url = 'https://new.land.naver.com/complexes/5039?ms=35.1618655,129.0321645,17&a=APT:JGC:ABYG&e=RETAIL'
res = requests.get(url)
res.raise_for_status() #문제 발생하면 오류를 알리고 종료
soup = BeautifulSoup(res.text, "lxml") # html parser 대신 lxml 사용

# with open("./quiz.html", "w", encoding = "utf8") as f:
#      f.write(soup.prettify()) # html 구조 파악하기 쉽게 설정
soup
soup.find('div', attrs = 'item_inner ')
soup.find('div')
