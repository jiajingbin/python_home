# encoding:utf-8
from PIL import Image
from selenium import webdriver
from time import sleep
url = 'http://192.168.56.1:9090'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)
# 截取当前网页并放到E盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot('E:\\printscreen.png') 
imgelement = driver.find_element_by_xpath(".//*[@id='prtImg']")  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
size = imgelement.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open("E:\\printscreen.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('E:\\save.png') # 保存我们接下来的验证码图片 进行打码
driver.close()
