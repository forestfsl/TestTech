#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 19:47
"""
from time import sleep

from selenium.webdriver.common.by import By

"""
打开页面:https://testerhome.com/
点击-社团标签
点击-霍格沃兹学院
访问顶部的第一个帖子
"""

from selenium import webdriver

class TestHogwards():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #隐式等待(动态等待，执行完就下一步，如果没有，就最多等到5秒，把下面sleep(3)注销)
        self.driver.implicitly_wait(5)
        pass

    def teardown(self):
        #加上这个，资源会回收，否则不会回收
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(by=By.LINK_TEXT, value="社团").click()
        #sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value="求职面试圈").click()
        #sleep(3)
        self.driver.find_element(by=By.CSS_SELECTOR, value=".topic-34625 .title > a").click()
        sleep(3)


"""
google 安装selenium-ide插件，在百度网盘我的应用数据里面，需要再终端解压
unzip selenium.zip -d selenium-ide
然后将selenium-ide 直接拖拽到chrome:://extensions中执行
之后店家google 点击selenium-ide 插件，点击run测试，然后在打开的浏览器中输入要测试的网址
然后就可以定位到元素了
"""



