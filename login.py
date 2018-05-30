# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import win32api
import win32con
import pytesseract
from PIL import Image
from pytesseract import *
driver = webdriver.Firefox()
#driver = webdriver.Ie()
driver.implicitly_wait(10)
sleep(3)
driver.get("http://192.168.56.1:9090")
sleep(3)
def username_get():
    driver.find_element_by_id("username").send_keys("safeadmin")
def passwd_get():
    driver.find_element_by_id("password").send_keys("wst!@#$1234")
def validatecode_get():

    right_click = driver.find_element_by_xpath(".//*[@id='prtImg']")

    sleep(2)
    #ActionChains(driver).context_click(right_click).send_keys(Keys.ARROW_DOWN).perform()
    ActionChains(driver).context_click(right_click).perform()
    print("debug1")
    sleep(3)
    win32api.keybd_event(83,win32con.KEYEVENTF_KEYUP,0)
    sleep(3)
    print("debug2")
    win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(89,win32con.KEYEVENTF_KEYUP,0)
def validatecode_pytesseract():
    rep={'O':'0',                           #替换列表
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };

    def initTable(threshold=140):           # 二值化函数
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table
    #--------------------------------------------------------------------------------------
    im = Image.open("D:\\1.gif")     #1.打开图片
    im = im.convert('L')                                        #2.将彩色图像转化为灰度图
    binaryImage = im.point(initTable(), '1')                    #3.降噪，图片二值化
    # binaryImage.show()
    vcode = image_to_string(binaryImage, config='-psm 7')
    #4.对于识别结果，常进行一些替换操作
    for r in rep:
        vcode = vcode.replace(r,rep[r])
    #5.打印识别结果
    return vcode
passwd_get()
username_get()

validatecode_get()
sleep(3)
validatecode = validatecode_pytesseract()
#print(validatecode)
driver.find_element_by_id("validateCode").send_keys(validatecode)
sleep(1)
driver.find_element_by_class_name("login_btn_out").click()
sleep(5)
