#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/30 22:41
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testcases.selenium_js.base import Base

"""
在页面操作中有时会遇到JavaScript所生成的alert，comfir与及prompt弹框，可以使用switch_to.alert()方法
定位到。然后使用text/accept/dismiss/send_keys等方法进行操作。分辨alert，window，div模态框，与及操作
操作alert常用的方法:
- switch_to.alert():获取当前页面上的警告框
- text:返回alert/comfirm/prompt中的文字信息
- accept() 接受现有警告框
- dismiss() 解散现有警告框
- send_keys(keysToSend):发送文本至警告框。keysToSend将文本发送至警告框

https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
"""

class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #因为这个控件在一个ifram中，所以需要先切换
        self.driver.switch_to_frame('iframeResult')


        drag = self.driver.find_element(by=By.ID,value="draggable")
        drop = self.driver.find_element(by=By.ID,value="droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        time.sleep(5)
        print("点击alert确认")
        #会出现一个弹框，这个时候需要切换到alert
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        #点击运行
        self.driver.find_element(by=By.ID,value="submitBTN").click()
        time.sleep(3)
