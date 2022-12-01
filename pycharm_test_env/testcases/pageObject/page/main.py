#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/1 23:35
"""
from selenium.webdriver.common.by import By

from testcases.pageObject.page.base_page import BasePage
from testcases.pageObject.page.login import Login
from testcases.pageObject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)


    def goto_login(self):
        return Login(self._driver)