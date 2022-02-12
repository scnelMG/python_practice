# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:51:03 2021

@author: 박민규
"""

import requests
from bs4 import BeautifulSoup
import re

# UserAgent 사용
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

# 예 - 쿠팡의 여러페이지 이동하며 크롤링(url의 특징을 이용)

# 페이지 여러개에서 불러오기

for i in range(1,6):
    print("페이지:",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
   
    
    for item in items:
        # 광고 제품은 제외
        ad = item.find("span", attrs={"class":"ad-badge-text"})
        if ad:
            #print("<광고 상품 제외>")
            continue
        
        name = item.find("div", attrs={"class":"name"}).get_text()
        # 한성컴퓨터 제품은 제외
        if "한성" in name:
            #print("<한성 제품 제외합니다>")
            continue
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            #print(" <평점 없는 상품 제외>")
            continue
        
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            #print(" <평점 수 없는 상품 제외>")
            continue
        link = item.find("a", {"class":"search-product-link"})["href"]
       
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        if float(rate)>=4.5 and int(rate_count)>=100:
            #print(name, price+"원", rate+"점", rate_count+"개")
            print(f"제품명 : {name}")
            print(f"가격 : {price}원")
            print(f"제품명 : {rate}점 ({rate_count}개)")
            print("해당 링크: https://www.coupang.com"+link)
            print("-"*50)
