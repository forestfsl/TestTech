#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/18 20:23
"""
from time import sleep

from testcases.data.test2.page.app import App


class TestSearch:
    def test_search(self):
        #App().start().main()
        App().start().main().goto_market().goto_search().search("jd")
        sleep(5)