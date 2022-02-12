# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:04:39 2021

@author: 박민규
"""

import requests
url ="http://nadocoding.tistory.com"

# 페이지에 들어갈 때 사용자인지, 봇인지 확인핧 때, 사용자로 인식하도록 하게 만듬 User-Agent
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)














