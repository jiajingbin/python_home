from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.56.1:9090")
sleep(2)
right_click = driver.find_element_by_xpath(".//*[@id='prtImg']")
#对定位到的元素执行鼠标右键操作
print(right_click.get_attribute("src"))
sleep(1)
ActionChains(driver).context_click(right_click).perform()
ActionChains(driver).context_click(right_click).perform()
ActionChains(driver).context_click(right_click).perform()
