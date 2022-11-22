#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 23:00
"""

import  allure
import pytest


"""
如果想通过命令行执行
pytest -v test_feature_story.py --allure-features '登录成功'

如果想执行指定的store名字
pytest -v test_feature_story.py --allure-features '登录成功' --allure-stories '登录成功'

-v 参数可以看到距离执行的案例
"""

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_success_a(selfself):
     print("这是登录：测试用例，登录失败")
    pass

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")

        pass

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("则是登录：测试用例，登录失败")
        pass

if __name__ == '__main__':
    pytest.main()


"""
allure特性-feature/story
注解@allure.feature 与 @allure.store 的关系
- feature 相当于一个功能，一个大的模块，将case分类到某个feature中，报告中
behaviore 中显示，相当于testsuite
- story 相当于对应这个功能或者模块下的不同场景，分支功能，属于feature之下的结构
，报告在features中显示，相当于testcase
- feature 与story类似于父子关系
"""