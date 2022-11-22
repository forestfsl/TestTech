#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/21 23:13
"""
import allure
import pytest
from selenium import  webdriver
import time
from selenium.webdriver.common.by import By

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
        with allure.step("打开百度网页"):
            # "/Users/fengsonglin/project/TestTech/pycharm_test_env/testcases/chromedriver.exe"
            driver = webdriver.Chrome()
            driver.get("http://www.baidu.com")
            driver.maximize_window()

        with allure.step(f"输入搜索词:{test_data1}"):
            driver.find_element(by=By.ID, value='kw').send_keys(test_data1)
            time.sleep(2)
            driver.find_element(by=By.ID, value='su').click()
            time.sleep(2)

        with allure.step("保存图片"):
            driver.save_screenshot("./result/b.png")
            allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

        with allure.step("退出浏览器"):
            driver.quit()

if __name__ == '__main__':
    pytest.main()


