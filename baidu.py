# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

"""获得输入框的尺寸"""
size = driver.find_element_by_css_selector("#kw").size
print(size)

"""返回百度页面底部备案信息"""
text = driver.find_element_by_css_selector("#cp").text
print(text)

"""返回元素的属性值"""
attribute = driver.find_element_by_css_selector("#kw").get_attribute("name")
print(attribute)

"""返回元素的结果是否可见，返回结果为True或False"""
result = driver.find_element_by_css_selector("#kw").is_displayed()
print(result)
