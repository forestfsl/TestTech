#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 18:34
"""
from selenium.webdriver.common.by import By

from testcases.selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(by=By.ID, value="draggable").text)
        #切换
        self.driver.switch_to.parent_frame()
        #self.driver.switch_to.default_content()
        print(self.driver.find_element(by=By.ID, value="submitBTN").text)




