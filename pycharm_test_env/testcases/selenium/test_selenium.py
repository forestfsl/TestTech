#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 15:33
"""

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
