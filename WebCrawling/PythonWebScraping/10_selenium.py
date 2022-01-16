# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:52:35 2021

@author: Mgyu
"""

from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:/Users/Mgyu/Desktop/PL/python/python YT/webscraping/chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
browser.forward()
browser.refresh()

# elem = browser.find_element_by_class_name("input_text")
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("오킹")
elem.send_keys(Keys.ENTER)

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
