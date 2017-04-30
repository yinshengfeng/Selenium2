# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

"""鼠标悬停"""
set = driver.find_element_by_partial_link_text("设置")
ActionChains(driver).move_to_element(set).perform()

"""打开搜索设置"""
driver.find_element_by_partial_link_text("搜索设置").click()
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()

"""接收弹窗"""
driver.switch_to_alert().accept()
