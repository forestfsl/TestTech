#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/21 22:53
"""
import  allure

"""
 pytest test_sevenrity.py --alluredir=./result/9 --allure-severities normal,critical

"""
def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trival_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass
