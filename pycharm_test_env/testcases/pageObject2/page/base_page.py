#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/1 23:36
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self,driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址(/Applications/Google\ Chrome.app/Contents/MacOS/Google\Chrome --remote-debugging-port=9222)
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self._driver = webdriver.Chrome(options=chrome_arg)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)


    def find(self, locator):
        # 解元祖的操作
        return self._driver.find_element(*locator)