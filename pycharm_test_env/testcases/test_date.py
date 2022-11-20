#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 19:07
"""
import  pytest
import  yaml

class TestData:
    #@pytest.mark.parametrize("a,b",[(10,20),(10,5),(3,9)])
    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a + b)

if __name__ == '__main__':
    pytest.main()