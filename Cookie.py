# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

"""获得cookie信息"""
cookie = driver.get_cookies()
print(cookie)
driver.add_cookie({"name": "key-aaaaa", "value": "value-aaaa"})
cookies = driver.get_cookies()
for ck in cookies:
    print(ck["name"], ck["value"])

driver.quit()