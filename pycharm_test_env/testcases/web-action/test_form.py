#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/29 23:04
"""
import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tear(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(by=By.ID, value='user_login').send_keys("123")
        self.driver.find_element(by=By.ID, value='user_password').send_keys("password")
        self.driver.find_element(by=By.CLASS_NAME, value='custom-control-label').click()
        self.driver.find_element(by=By.XPATH,value='//*[@id="new_user"]/div[4]/input').click()
        sleep(5)

if __name__ == '__main__':
    pytest.main()
