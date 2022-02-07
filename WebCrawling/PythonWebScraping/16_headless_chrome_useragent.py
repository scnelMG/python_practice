# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:51:01 2022

@author: Mgyu
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
# user agent를 지정해주면 HeadlessChrome 대신 Chrome이라고 뜸


browser = webdriver.Chrome(options = options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text) # HeadlessChrome 이라고 뜸
browser.quit()