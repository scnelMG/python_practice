# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:16:38 2021

@author: 박민규
"""

import requests
from bs4 import BeautifulSoup

#네이버 웹툰
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.get_text())
print(soup.a.attrs) # a element의 속성정보를 출력
print(soup.a["href"]) # a element의 href 속성'값'정보를 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# find: 뒤 정보에 해당하는 첫 element 가져옴
# class="Nbtn_upload" 인 a element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"}))
# class="Nbtn_upload" 인 element를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
rank1 =soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling) # 다음 element로 넘어감
print(rank1.next_sibling.next_sibling) 
# 두번 next_sibling 해야 다음으로 넘어갔음 => 줄바꿈 떄문
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.get_text())    

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())  

print(rank1.parent)

rank2 = rank1.find_next_sibling("li") #괄호 안 조건에 맞는 것만 찾음
print(rank2.a.get_text())  
rank3 = rank2.find_next_sibling("li")
rank4 = rank3.find_next_sibling("li")
print(rank3.a.get_text()) 
print(rank4.a.get_text()) 
rank3 = rank4.find_previous_sibling("li")
print(rank3.a.get_text()) 

ranking = rank1.find_next_siblings("li")
for i in ranking:
    print(i.a.get_text()) 
# siblings는 list로 저장되어서 그런듯

print(ranking)
webtoon = soup.find("a", text="조조코믹스-킹스앱스 END")
# text에 해당하는 a태그 찾음
print(webtoon) 
# <a onclick="nclk_v2(event,'rnk*p.cont','774862','2')"
#  href="/webtoon/detail?titleId=774862&amp;no=20" 
#  title="조조코믹스-킹스앱스 END">조조코믹스-킹스앱스 END</a>

#%%
























