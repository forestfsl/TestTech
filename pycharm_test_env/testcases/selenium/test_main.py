#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/1 23:20
"""
from testcases.selenium.main import Main


class TestMain:
    def setup(self):
        main = Main()
        main.click_first_link().title()