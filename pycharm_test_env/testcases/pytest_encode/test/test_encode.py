#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 10:59
"""
import pytest

from testcases.pytest_encode.pytest_encode import encode_logger


@pytest.mark.parametrize("name",["侧石2222","测试信息"])
def test_mm(name):
    encode_logger.info("测试编码")
    print(name)