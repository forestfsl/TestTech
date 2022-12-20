#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/19 22:11
"""
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_cap = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': 'emulator-5554',
            'chromedriverExecutable': '/Users/fengsonglin/Documents/chromedriver'
        }
        # des_cap = {}
        # des_cap['platformName'] = 'Android'
        # des_cap['platformVersion'] = '6.0'
        # des_cap['deviceName'] = 'emulator-5554'
        # des_cap['browserName'] = 'Browser'
        # des_cap['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        element = self.driver.find_element(by=By.CLASS_NAME,value="fake-placeholder")
        element.click()
        #self.driver.find_element(by=By.XPATH,value="//*[@id='index-kw']").click()
        sleep(5)
        self.driver.find_element(by=By.ID,value="index-kw").send_keys("appium")
        search_locator = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()