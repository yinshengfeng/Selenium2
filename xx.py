# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

right_click=driver.find_element_by_css_selector("#kw")

"""定位到右击的元素"""
ActionChains(driver).context_click(right_click).perform()