from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# init
url = 'http://192.168.56.1:9090'
xpath = ".//*[@id='prtImg']"

# set profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', 'D:\\')
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/jpeg')

# launch driver
driver = webdriver.Firefox(firefox_profile=fp)
driver.get(url)

for element in driver.find_elements_by_xpath(xpath):
    img_url = element.get_attribute('src')
    img_desc = element.get_attribute('data-desc')

    action = ActionChains(driver).move_to_element(element)
    action.context_click(element)
    action.send_keys(Keys.ARROW_DOWN)                
    action.send_keys('v')
    action.perform()
    # click save image

