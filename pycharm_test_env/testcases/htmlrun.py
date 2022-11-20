#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 13:24
"""
import unittest

from util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'

    test_dir = '../testcases'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)