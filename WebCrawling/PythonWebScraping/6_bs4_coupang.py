# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:32:34 2021

@author: 박민규
"""

# 예 - 쿠팡
import requests
from bs4 import BeautifulSoup
import re

# UserAgent 사용
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
res = requests.get(url, headers = headers)

res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("dl", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    # 광고 제품은 제외
    ad = item.find("span", attrs={"class":"ad-badge-text"})
    if ad:
        print("<광고 상품 제외>")
        continue
    name = item.find("div", attrs={"class":"name"}).get_text()
    # 한성컴퓨터 제품은 제외
    if "한성" in name:
        print("<한성 제품 제외합니다>")
        continue
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외>")
    rate_count = item.find("span", attrs={"class":"rating-total-count"})
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1] # 괄호 제외하기
        
    else:
        print(" <평점 수 없는 상품 제외>")
        continue
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    if float(rate)>=5 and int(rate_count)>=1000:
        print(name, price+"원", rate+"점", rate_count+"개")
        

    
