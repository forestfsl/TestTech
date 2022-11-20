#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 20:03
"""
import pytest
import yaml

class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是", env["dev"])