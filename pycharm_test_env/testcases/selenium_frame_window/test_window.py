#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 16:32
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from testcases.selenium_frame_window.base import Base
from time import  sleep

"""
打印窗口的数据
CDwindow-128EAF3C316759C7627434002403B5B7
['CDwindow-128EAF3C316759C7627434002403B5B7', 'CDwindow-8E881186F3CCE37A9B63FD526F3D9F01']

"""

#TANGRAM__PSP_4__userName
#TANGRAM__PSP_4__phone
class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(by=By.LINK_TEXT, value="登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element(by=By.LINK_TEXT, value="立即注册").click()
        #这里如果直接这样使用会爆出 self.driver.find_element(by=By.ID, value='TANGRAM__PSP_4__userName').sendkeys("username")
        #因为是切换到一个新的窗口来实现的，self.driver还是当前的
        #self.driver.find_element(by=By.ID, value='TANGRAM__PSP_4__userName').sendkeys("username")
        print(self.driver.current_window_handle)
        #打印所有窗口的名字
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(by=By.ID, value='TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element(by=By.ID, value='TANGRAM__PSP_4__phone').send_keys("phone")
        sleep(5)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__changeSmsCodeItem").click()
        sleep(5)
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__changePwdCodeItem").click()
        sleep(5)
        self.driver.find_element(by=By.ID, value='TANGRAM__PSP_11__userName').send_keys("login_username")
        self.driver.find_element(by=By.ID, value='TANGRAM__PSP_11__password').send_keys("login_password")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()
        sleep(5)
