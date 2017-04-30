#coding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("hello")
driver.find_element_by_css_selector("#su").submit()