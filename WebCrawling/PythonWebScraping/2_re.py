# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:34:24 2021

@author: 박민규
"""
#%% 정규식 1
# 주민등록번호
# 010328-3111111

# 이메일 주소
# sdfdsfsdf@gmail.com

# 차량 번호
# 11가 1234

# IP 주소
# 111.111.1.1

import re
# abcd, book, dest - 4글자
# ca?e
# care, cafe, case ...

p = re.compile("ca.e") # .은 하나의 문자를 의미 > cafe, care (O)| caffe  (X)
# ^: 문자열의 시작 > (^de) : desk, destination (O) | fade (X)
# $: 문자열의 끝 > (se$) : case, base (O) | face (X)

m = p.match("case")
# m1 = p.match("caffe")
print(m.group()) #매치되지 않으면 에러 발생
# print(m1.group()) 
def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력반은 문자열 출력
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작/ 끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless")
# match : 주어진 문자열의 처음부터 일치하는지 확인, 
# 즉 뒤에 뭐 있어도 매칭되었다고 함
print_match(m)

m = p.search("good care")
# search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

m = list = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(list)
#%% 정리
1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열 ") : 주어진 문자열의 처음부터 일치하는지 확인, 
3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
4. list = p.findall("비교할 문자열") 일치하는 모든 것을 "리스트" 형태로 반환

원하는 형태 : 정규식
.은 하나의 문자를 의미 > cafe, care (O)| caffe  (X)
^: 문자열의 시작 > (^de) : desk, destination (O) | fade (X)
$: 문자열의 끝 > (se$) : case, base (O) | face (X)










