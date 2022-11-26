#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/22 21:58
"""
import logging
from typing import List

import pytest
import yaml

"""
site-package->_pytest->hookspec.py
"""


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filename='my.log',
                    filemode='w'
                    )

encode_logger = logging.getLogger(__name__)

def pytest_collection_modifyitems(session,config,items:List):
    for item in items:
        # item.name 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        #测试用例里面有login单词，就加上一个login的标签
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    items.reverse()
