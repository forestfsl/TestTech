#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/30 22:33
"""
import time

from selenium.webdriver.common.by import By

from testcases.selenium_js.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(by=By.CLASS_NAME,value="soutu-btn").click()
        self.driver.find_element(by=By.CLASS_NAME,value="upload-pic").send_keys("/Users/fengsonglin/Pictures/Snip20221127_9.png")
        time.sleep(5)