#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 16:34
"""
from selenium import webdriver

class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        pass

    def teardown(self):
        pass
