#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/25 18:10
"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaohu:
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '6.0'
        #deviceName 这个属性并不能说明一个什么东西，因为默认会使用adb devices 命令下第一个的来运行，
        #这里这个属性只是一个解释性文字，改成aaa也可以的，任意的，如果adb devices下面有多个设备，想指定的话，需要通过uuid
        desire_caps['deviceName'] = 'emulator-5556'
        desire_caps['udid'] = 'emulator-5556'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.mainnesting.view.MainNestingActivity'
        #noReset fullreset dontStopAppOnReset
        desire_caps['noReset'] = "true"
        desire_caps['unicodeKeyBoard'] = "true"
        desire_caps['resetKeyBoard'] = "true"
        desire_caps['chromedriverExecutable'] = '/Users/fengsonglin/Documents/chromedriver'
        # 首次启动不停止app
        desire_caps['dontStopAppOnReset'] = "true"
        desire_caps['skipServerInstallation'] = 'true'
        desire_caps['skipDeviceInitialzation'] = 'true'
        #授权
        desire_caps['autoGrantPermissions'] = True
        #超时属性 5分钟内都不会超时
        desire_caps['newCommandTimeout'] = 300
        #下面这个参数用来启动模拟器,名字填写emulator -list-avds 中看到的名字
        desire_caps['avd'] = 'Pixel_XL_API_33'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    #需要使用emulator获取模拟器，mumu模拟器不支持
    def test_mobile(self):

        #加入录屏功能(8.0)版本才支持
        self.driver.start_recording_screen()
        self.driver.make_gsm_call('15013339531',GsmCallActions.CALL)
        self.driver.send_sms('15013339531','test' )
        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
        self.driver.get_screenshot_as_file('./photos/img.png')

        #10秒之后停止录屏
        sleep(10)
        self.driver.stop_recording_screen()
