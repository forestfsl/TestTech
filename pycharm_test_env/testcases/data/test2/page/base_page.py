#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/18 17:45
"""
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    #解决弹窗这种事情的黑名单
    _black_list=[(By.ID,"image_cancel")]
    _error_count=0
    _error_max=0
    _params={}
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self,by,locator=None):
        isTuple = bool(isinstance(by, tuple))
        try:
            element = self._driver.find_elements(*by) if isTuple else self._driver.find_element(by,locator)
            self._error_count=0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by,locator)
            raise e

    def send(self,value,by, locator=None):
        try:
            self.find(by,locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value,by,locator)
            raise

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    by = step["by"]
                    locator = step["locator"]
                    element = self.find(step["by"],step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        #{value}
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param,self._params[param])
                        self.send(content,step["by"],step["locator"])


    def teardown(self):
        self._driver.back()
        self._driver.quit()