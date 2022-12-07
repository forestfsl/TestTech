#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/7 23:05
"""
from appium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

desire_caps={}
desire_caps['platformName']='Android'
desire_caps['platformVersion']='6.0'
desire_caps['deviceName']='emulator-5554'
desire_caps['appPackage']='com.xueqiu.android'
desire_caps['appActivity']='.mainnesting.view.MainNestingActivity'
desire_caps['noReset']="true"
#首次启动不停止app
desire_caps['dontStopAppOnReset']="true"
desire_caps['skipDeviceInitialzation']='true'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
driver.implicitly_wait(10)
#driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout").click()

driver.find_element(by=By.ID,value="com.xueqiu.android:id/home_search").click()
driver.find_element(by=By.ID,value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
sleep(10)
driver.back()
driver.back()
driver.quit()