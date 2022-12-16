#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/16 21:52
"""
from appium.webdriver.common.mobileby import MobileBy

"""
获取当前activity
[21:53:17][~/project/TestTech]$ adb devices
List of devices attached
emulator-5554	device

[21:53:24][~/project/TestTech]$ adb shell dumpsys window | grep mCurrent
    mCurrentAppOrientation=-1
      mCurrentRotation=0
        mCurrentUserId=0
  mCurrentFocus=Window{d63bdbf u0 com.touchboarder.android.api.demos/com.example.android.apis.view.PopupMenu1}
"""

from appium import webdriver

class TestToast():
    def setup(self):
        desire = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.touchboarder.android.api.demos',
            'appActivity': 'com.example.android.apis.view.PopupMenu1',
            'dontStopAppOnReset': 'true',
            'skipDeviceInitialzation':'true'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        #通过uiautomatorviewer 查找元素text
        #如果content-desc 有值，可以使用ACCESSIBILITY_ID来取值，否则只有text的话，可以考虑用xpath
        #self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Search']").click()
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)



