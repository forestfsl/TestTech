#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/5 00:09
"""
from appium import webdriver
"""
[0:14:23][~]$ adb devices
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached
emulator-5554	offline
"""
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()
