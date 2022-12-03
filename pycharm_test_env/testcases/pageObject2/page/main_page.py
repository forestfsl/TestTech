#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/2 21:21
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from testcases.pageObject2.page.add_member_page import AddMemberPage
from testcases.pageObject2.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 元素定位封装成了一个元祖
    add_member_ele = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    def goto_add_member(self):
        self.find(self.add_member_ele).click()
        return AddMemberPage(self._driver)

    def goto_contact(self):
        pass