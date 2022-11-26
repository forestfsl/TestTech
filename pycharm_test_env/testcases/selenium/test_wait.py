#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 21:59
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.implicitly_wait(3)

    #title = "原创精华文章,有100元奖金"
    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="原创精华文章,有100元奖金"]').click()

        #方式1：
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@class="navigation-controls"]')) >= 1

        WebDriverWait(self.driver,10).until(wait)

        #方式2
        #WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))

        self.driver.find_element(By.XPATH, '//*[@title="招聘内推"]').click()
        print("hello")
