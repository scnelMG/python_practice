# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:47:35 2021

@author: Mgyu
"""

no = int(input("어느 범위에서 소수를 구하고 싶은가요?")) # 원하는 범위 설정

l_no = list(range(2, no+1)) # 원하는 숫자가 있는 list 생성

for k in range(0, no-1):
    i = k+2  #i는 2부터 체크

    inc=2

    temp=i*inc

    while temp <= no:
        if temp in l_no:
            l_no.remove(temp)
        inc=inc+1
        temp=i*inc

print("찾아낸 소수: {}, 총 {}개".format(l_no,len(l_no)))
# %%


Prime =list(range(2, 101)) # 2~100까지 숫자 나열
print(Prime)
for k in range(0,99):
    i = k+2 # 2부터 시작
    inc= 2 #inc - 증가량
    temp=i*inc # temp - 제거 대상 정하기 (2,3,... 의 배수를 삭제)
    
    while temp <= 100:
        if temp in Prime:
            Prime.remove(temp) # 소수 아닌 수 제거 
        inc+=1
        temp=i*inc
print("찾아낸 소수: {}, 총 {}개".format(Prime,len(Prime)))
    
    
