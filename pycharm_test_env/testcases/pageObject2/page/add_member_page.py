#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/2 21:21
"""
from selenium.webdriver.common.by import By

from testcases.pageObject2.page.base_page import BasePage
from testcases.pageObject2.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self,name,account,phone):
        # 添加姓名、 账号、 手机号
        self._driver.find_element(By.ID, "username").send_keys(name)
        self._driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        self._driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        # 点击保存
        self._driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        return ContactPage(self._driver)

    def add_member_fail(self, name,account,phone):
        self._driver.find_element(By.ID, "username").send_keys(name)
        self._driver.find_element(By.ID, "memberAdd_acctid").send_keys("11122")
        self._driver.find_element(By.ID, "memberAdd_phone").send_keys("13199991111")
        # 点击保存
        self._driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        ele_list = self._driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in ele_list]
        print(error_list)

    def goto_contact(self):
        pass