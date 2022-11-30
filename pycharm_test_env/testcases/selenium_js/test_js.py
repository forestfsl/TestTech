#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/30 21:38
"""
import time

import pytest
from selenium.webdriver.common.by import By

from testcases.selenium_js.base import Base


class TestJS(Base):
    @pytest.mark.skip
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

    """
    打开网址https://www.12306.cn/index/
    修改出发日期为2022-01-01
    打印出发日期
    关闭网址
    """
    def test_js_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        #用js去掉readonly属性，然后直接输入日期文本
        date_js="document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date_js)
        time.sleep(2)
        date_js_1 = "document.getElementById('train_date').value='2023-01-01'"
        self.driver.execute_script(date_js_1)
        print("打印")
        print('f当前打印日志:{self.driver.find_element(by=By.ID,value="train_date")')
        time.sleep(5)

