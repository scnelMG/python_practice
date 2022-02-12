# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:52:35 2021

@author: Mgyu
"""

from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 창 뒤로가기, 앞르로가기, 새로고침
browser.back()
browser.forward()
browser.refresh()
browser.back()

# elem = browser.find_element_by_class_name("input_text")
# 검색창에 원하는 검색어 입력
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("오킹")
elem.send_keys(Keys.ENTER)

browser.back()

elem = browser.find_elements_by_tag_name("a")
elem
for e in elem:
    e.get_attribute("href")
    

browser.get("http:/daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("오킹")
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()
browser.quit()
