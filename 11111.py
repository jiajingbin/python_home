from selenium import webdriver
driver = webdriver.Ie()
driver.get("http://www.baidu.com")
size = driver.find_element_by_id('kw').size
print(size)
