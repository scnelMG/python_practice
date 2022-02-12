# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:16:58 2021

@author: 박민규
"""

import requests
res = requests.get("http://google.com") # 원하는 링크 입력
print("응답코드: ", res.status_code) #200이면 정상
# res_2 = requests.get("http://nadocoding.tistory.com")
# print("응답코드: ", res_2.status_code) #200이면 정상 403이면 권한 없음


# if res.status_code == requests.codes.ok:
    # print("정상입니다.")
# else:
    # print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status() #문제 발생하면 오류를 알리고 종료
print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("./mygoogle.html", "w", encoding="utf8") as f: # html 내용을 파일로 저장
    f.write(res.text)

