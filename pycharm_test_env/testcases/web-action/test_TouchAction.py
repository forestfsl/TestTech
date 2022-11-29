#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/28 22:53
"""
import pytest
from selenium.webdriver.common.by import By

"""
打开Chorme->打开URL:http://www.baidu.com
向搜索框中输入'selenium测试',通过TouchAction点击搜索框，滑动到底部，点击下一页
光比Chorme
"""

from selenium import webdriver
from selenium.webdriver import TouchActions
from  time import  sleep

class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element(by=By.ID,value='kw')
        print(el)
        el_search = self.driver.find_element(by=By.ID,value='su')

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el,0,10000).perform()
        sleep(5)


if __name__ == '__main__':
    pytest.main()