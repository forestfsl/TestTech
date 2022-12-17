#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/17 23:22
"""
import pytest
from appium import webdriver
from hamcrest import assert_that, close_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:
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
        # 首次启动不停止app
        desire_caps['dontStopAppOnReset'] = "true"
        desire_caps['skipDeviceInitialzation'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        #self.driver.quit()

    #如果我除开想搜索aliba还想搜索小米的话，那么我是否需要重新起一个测试用例？是不需要的，我们可以通过测试化参数定制

    @pytest.mark.parametrize('searchkey,type,expect_price', [
        ('aliba','BABA',87),
        ('xiaomi','01810',10)
    ])
    def test_search(self,searchkey,type,expect_price):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入搜索词，比如alibaba or xiaomi ...
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        """
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(by=By.ID,value="com.xueqiu.android:id/name").click()
        locator = (By.XPATH, f"//*[@text='{type}']/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)

        # WebDriverWait(self.driver,10).until( lambda x: x.find_element(*locator)) 相当于上面两条语句叠加
        current_price = float(ele.text)
        print(f"当前{type}对应的股价价格是:{current_price}")
        #expect_price = 87.0
        assert_that(current_price,close_to(expect_price,expect_price * 0.1))