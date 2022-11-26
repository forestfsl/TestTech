#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/22 21:56
"""
import  pytest

@pytest.mark.parametrize("name",["侧石","测试信息"])
def test_mm(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login")
    assert False

def test_search():
    print("search")

"""
(venv) [9:47:58][~/project/TestTech/pycharm_test_env/testcases/test_pytest]$ pytest --env dev test_mm.py::test_env -vs
========================================== test session starts ==========================================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases/test_pytest
plugins: allure-pytest-2.11.1
collected 1 item                                                                                        

test_mm.py::test_env dev 环境
dev
PASSED

=========================================== 1 passed in 0.02s ===========================================
(venv) [9:48:20][~/project/TestTech/pycharm_test_env/testcases/test_pytest]$ 

"""
def test_env(cmdoption):
    #print(cmdoption)
    env,datas = cmdoption;
    print(datas)
   # print(datas['evn'])
    hosts = datas['env']['hosts']
    port = datas['env']['port']
    url = str(hosts) + ":" + str(port)
    print(url)

if __name__ == '__main__':
    pytest.main()