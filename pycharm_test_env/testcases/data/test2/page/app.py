#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/18 20:02
"""
from appium import webdriver
from testcases.data.test2.page.base_page import BasePage
from testcases.data.test2.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".mainnesting.view.MainNestingActivity"
        if self._driver is None:
            desire_caps = {}
            desire_caps['platformName'] = 'Android'
            desire_caps['platformVersion'] = '6.0'
            desire_caps['deviceName'] = 'emulator-5554'
            desire_caps['appPackage'] = _package
            desire_caps['appActivity'] = _activity
            desire_caps['noReset'] = "true"
            desire_caps['unicodeKeyBoard'] = "true"
            desire_caps['resetKeyBoard'] = "true"
            desire_caps['autoGrantPermissions'] = "true"
            # 首次启动不停止app
            desire_caps['dontStopAppOnReset'] = "true"
            desire_caps['skipDeviceInitialzation'] = 'true'
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)
        return self


    def main(self):
        return Main(self._driver)