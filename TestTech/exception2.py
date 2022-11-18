#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:10
"""
x = 10
if x>5:
    raise Exception("这是抛出的异常")

class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise  MyException("value1","value2")