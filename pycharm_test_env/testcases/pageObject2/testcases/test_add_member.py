#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/2 21:59
"""
import random

import pytest
import string
from testcases.pageObject2.page.main_page import MainPage


class TestAddMemer:

    def setup_class(self):
        self.main = MainPage()

    #@pytest.mark.parametrize("name", ["皮城女警"])
    def test_add_member(self):
        """
        用来测试添加成员
        :return:
        """
        randomStr = random.sample(string.ascii_letters + string.digits, 10)
        randomAccount = random.sample(string.digits,10)
        randomPhone = 15013339532

        #1.跳转到添加成员页面 2.添加成员 3.获取成员列表，做断言验证
        res = self.main.goto_add_member().add_member(randomStr,randomAccount,randomPhone).get_list()
        print(''.join(randomStr))
        assert ''.join(randomStr) in res

    def test_add_member_fail(self):
        self.main.goto_add_member().add_member_fail("Gf56Z","11122",15876398681)


if __name__ == '__main__':
    pytest.main()