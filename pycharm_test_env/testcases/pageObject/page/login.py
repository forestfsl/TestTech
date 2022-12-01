#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/1 23:49
"""
from selenium.webdriver.common.by import By

from testcases.pageObject.page.base_page import BasePage
from testcases.pageObject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Register(self._driver)
