# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
js_ = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
