#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/18 20:13
"""
from testcases.data.test2.page.Search import Search
from testcases.data.test2.page.base_page import BasePage


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)