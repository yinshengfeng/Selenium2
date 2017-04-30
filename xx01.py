# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

"""定位到悬停的元素"""

set = driver.find_element_by_partial_link_text("设置")
more = driver.find_element_by_partial_link_text("更多产品")
ActionChains(driver).move_to_element(set).perform()
# ActionChains(driver).move_to_element(more).perform()
