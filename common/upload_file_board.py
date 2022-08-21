from selenium import webdriver
import time
import clipboard
from pynput.keyboard import Controller,Key

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
clipboard.copy('name')
driver.find_element_by_name('wd').click()
time.sleep(0.5)


kb = Controller()
#实例化控制键盘
with kb.pressed(
    Key.ctrl,
    'v'
):
    pass
# 摁下黏贴
with kb.pressed(Key.enter):pass


