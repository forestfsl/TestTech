#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 13:11
"""
import unittest

if __name__ == '__main__':
    test_dir = '../testcases'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)