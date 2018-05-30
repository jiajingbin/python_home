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
driver.implicitly_wait("10")
