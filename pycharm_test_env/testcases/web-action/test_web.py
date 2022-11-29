#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/27 21:35
"""
import pytest

"""
ActionChains 用法
- 测试案例一
打开页面(http://sahitest.com/demo/clicks.htm)
分别对按钮'click me'，'dbl click me','right click me'执行点击
，双击，右键操作，打印上面展示框中的内容
"""

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import  sleep

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(7)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    #这个用例如果不想执行的话，就直接加上@pytest.marks.skip
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,"//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH,"//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH,"//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(5);
        action.perform()
    @pytest.mark.skip
    def test_moveto_element(self):
        self.driver.get("http://www.baidu.com")
        #s - usersetting - top
        ele = self.driver.find_element(by=By.ID, value='s-usersetting-top')
        #ele = self.driver.find_element(by=By.LINK_TEXT,value="设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(4)
#https://sahitest.com/demo/dragDropMooTools.htm
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(by=By.ID,value="dragger")
        drop_element = self.driver.find_element(by=By.XPATH,value="/html/body/div[2]")
        action = ActionChains(self.driver)
       # action.drag_and_drop(drag_element,drop_element)
        action.click_and_hold(drag_element).release(drop_element)
        #action.click_and_hold(drag_element).move_to_element(drop_element).release()
        action.perform()
        sleep(5)

#http://sahitest.com/demo/label.htm
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(by=By.XPATH,value="/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)




if __name__ == '__main__':
    pytest.main('-v','-s','test_web.py')
    #或者pytest test_web.py -v -s

