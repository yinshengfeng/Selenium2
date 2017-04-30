# coding=utf-8
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.implicitly_wait(10)

print("Before login=======================")

"""打印当前页面的title"""
print(driver.title)

"""打印当前页面的URL"""
now_url = driver.current_url
print(now_url)

"""执行邮箱登录"""
driver.switch_to_frame(driver.find_element_by_css_selector("#x-URS-iframe"))
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("selenium88")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456abc")
driver.find_element_by_css_selector("#dologin").click()

print("After login =========================")

"""再次打印当前页面的title"""
print(driver.title)
"""打印当前页面的URL"""
now_url = driver.current_url
print(now_url)

"""获取登录的用户名"""
sleep(10)
text = driver.find_element_by_css_selector("span#spnUid").get_attribute()
print(text)
