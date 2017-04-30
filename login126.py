# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.switch_to_frame(driver.find_element_by_css_selector("#x-URS-iframe"))
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("selenium88")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456abc")
driver.find_element_by_css_selector("#dologin").click()
