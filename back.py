# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

"""访问百度首页"""
first_url = "http://www.baidu.com"
print("now access" + first_url)
driver.get(first_url)

"""访问新闻页面"""
second_url = "http://news.baidu.com"
print("now access" + second_url)
driver.get(second_url)

"""返回到百度首页"""
print("反回到百度首页"+first_url)
driver.back()

"""前进到新闻页"""
print("前进到"+second_url)
driver.quit()