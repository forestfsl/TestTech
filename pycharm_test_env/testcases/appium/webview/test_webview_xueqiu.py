#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/20 19:01
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = 'emulator-5554'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.mainnesting.view.MainNestingActivity'
        desire_caps['noReset'] = "true"
        desire_caps['unicodeKeyBoard'] = "true"
        desire_caps['resetKeyBoard'] = "true"
        desire_caps['chromedriverExecutable'] = '/Users/fengsonglin/Documents/chromedriver'
        # 首次启动不停止app
        desire_caps['dontStopAppOnReset'] = "true"
        desire_caps['skipServerInstallation'] = 'true'
        desire_caps['skipDeviceInitialzation'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        # 这里要是text 包含我的，有多个地方出现，那么久回定义不到，这个时候，我们就可以考虑采取使用resourceId，结合text处理
        # self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR,value='new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("我的")').click()
        #com.xueqiu.android: id / title
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().textContains("股票")').click()
        print(self.driver.contexts)
        #print(self.driver.current_window_handle)
        A_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("立即开户")')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(A_locator))
        self.driver.find_element(*A_locator).click()
        #打印窗口看看有没有切换(>phonenumber_locator = (MobileBy.ID, 'phone-number') 出现这个情况找不到)
       # print(self.driver.window_handles)
        print(self.driver.contexts)
        print(self.driver.current_window_handle)
        #kaihu_window = self.driver.window_handles[-1]
        #self.driver.switch_to.context(self.driver.contexts[-1])
        #显式等待
        #phonenumber_locator = (MobileBy.ID, 'phone-number')
        phonenumber_locator1 = (MobileBy.XPATH, "phone-/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText")
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(phonenumber_locator1))

        self.driver.find_element(*phonenumber_locator1).send_keys("15013339532")
        #self.driver.find_element(MobileBy.ID,'code').send_keys("1234")
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.EditText').send_keys("1234")
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("立即开户")').click()

