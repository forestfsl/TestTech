#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/1 23:30
"""
from testcases.pageObject.page.main import Main

"""
1.立即注册
- 点击立即注册
- return 立即注册pageObject
2.企业登录
- 点击企业登录
- return 企业登录pageObject
"""
class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()