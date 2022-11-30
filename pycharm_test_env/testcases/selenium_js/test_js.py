#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/30 21:38
"""
import time

from selenium.webdriver.common.by import By

from testcases.selenium_js.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(by=By.ID,value="kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        js = "var action=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(20)
        js = "var action=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        self.driver.find_element(by=By.XPATH,value="//*[@id='page']/div/a[10]").click()
        time.sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))