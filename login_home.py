# coding=utf-8
from selenium import webdriver
from time import sleep
import pytesseract
from PIL import Image
from pytesseract import *
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.56.1:9090")
sleep(3)
def username_get():
    driver.find_element_by_id("username").send_keys("safeadmin")
def passwd_get():
    driver.find_element_by_id("password").send_keys("wst!@#$1234")
def validatecode_get():
    driver.save_screenshot('E:\\printscreen.png') 
    imgelement = driver.find_element_by_xpath(".//*[@id='prtImg']")  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open("E:\\printscreen.png")  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('E:\\save.png') # 保存我们接下来的验证码图片 进行打码
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
    im = Image.open("E:\\save.png")     #1.打开图片
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
