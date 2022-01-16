# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:57:34 2021

@author: Mgyu
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
browser = webdriver.Chrome(executable_path="C:/Users/Mgyu/Desktop/PL/python/python YT/webscraping/chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')))

browser.find_element
elem = browser.find_element_by_class_name("tabContent_option__2y4c6 select_Date__1aF7Y")
elem.click()



