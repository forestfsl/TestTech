#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/21 22:38
"""

import allure

@allure.link("https://www.baidu.com",name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment->268313637'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass

"""
pytest test_alluredemo_link_issue.py --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{} --alluredir=./result/8

"""
#--allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue(140,'这是一个issue')
def test_with_issue_link():
    pass
