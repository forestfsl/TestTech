#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/5 00:09
"""
import pytest
from appium import webdriver
"""
[0:14:23][~]$ adb devices
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached
emulator-5554	offline

m1 电脑，可以安装android studio 然后下载sdk
 ~/Documents/appium-enviroment/android-sdk-macosx  emulator -list-avds
Pixel_3a_API_31_arm64-v8a
 ~/Documents/appium-enviroment/android-sdk-macosx  emulator -avd Pixel_3a_API_31_arm64-v8a
"""

"""
若是adb devices 没有输出东西，可以用下面指令连接
[22:16:37][~]$ adb connect 127.0.0.1:5555 
"""
class TestAppium:
    def test_firstappium_demo(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #m1 电脑12 mac pro 6
        desired_caps['platformVersion'] = '6'
       # desired_caps['platformVersion'] = '12'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = 'com.android.settings.Settings'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.quit()

if __name__ == '__main__':
    pytest.main()



