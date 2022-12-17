#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/17 19:05
"""
import pytest
from hamcrest import *

class TestAssert():
    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        assert a > b
        assert 'h' in 'this'


    def test_hamrest(self):
        #assert_that(10, equal_to(9), '这是一个提示')
        assert_that(86.79,close_to(87,2))
        assert_that("contains some string", contains_string("string"))