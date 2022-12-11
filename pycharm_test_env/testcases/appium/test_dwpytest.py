#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/10 11:03
"""
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from time import  sleep

class TestDw():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = 'emulator-5554'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.mainnesting.view.MainNestingActivity'
        desire_caps['noReset'] = "true"
        desire_caps['unicodeKeyBoard'] ="true"
        desire_caps['resetKeyBoard'] = "true"
        # 首次启动不停止app
        #desire_caps['dontStopAppOnReset'] = "true"
        desire_caps['skipDeviceInitialzation'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1.打开雪球app
        2.点击搜索框
        3.向搜索框里面输入阿里巴巴
        4.在搜索结果里选择阿里巴巴，然后进行点击(appium inspector 通过xpath获取//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']，因为通过id获取有多个元素)
        5.获取 阿里巴巴的股价，并判断这只股价的价格>90
        如果是android 可以考虑用
        [18:49:57][~/project/TestTech]$ which uiautomatorviewer
/Users/fengsonglin/android-sdk-macosx/tools/uiautomatorviewer
        """
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        ele = self.driver.find_element(by=By.XPATH,value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        """
        这里当前价格为什么不通过android.widget.TextView 来定义i，是因为这个地方有多处调用
        """
        current_price = float(self.driver.find_element(by=By.ID,value="com.xueqiu.android:id/current_price_dtv").text)
        assert current_price > 90
        sleep(3)

    @pytest.mark.skip
    def test_attr(self):
        """
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入:alibaba
        判断【阿里巴巴】是否课件
        如果课件 打印搜索成功，如果不可见，打印搜索失败
        appium-uiautomator2-server 源码
        :return:
        """
        element = self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element(by=By.XPATH, value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            print(alibaba_element.get_attribute("displayed"))
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")


    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        sleep(4)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()



if __name__ == '__main__':
    pytest.main()