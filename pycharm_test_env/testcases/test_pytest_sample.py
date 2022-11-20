#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 17:52
"""
import pytest

"""
(venv) [18:03:26][~/project/TestTech/pycharm_test_env/testcases]$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases
collected 10 items                                                             

test_pytest_sample.py F                                                  [ 10%]
test_search.py ...                                                       [ 40%]
test_unittest.py ......                                                  [100%]

=================================== FAILURES ===================================
_________________________________ test_answer __________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_pytest_sample.py:12: AssertionError
=========================== short test summary info ============================
FAILED test_pytest_sample.py::test_answer - assert 4 == 5
========================= 1 failed, 9 passed in 0.06s ==========================

(venv) [18:21:46][~/project/TestTech/pycharm_test_env/testcases]$ pytest  test_pytest_sample.py -v
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases
collected 2 items                                                              

test_pytest_sample.py::test_answer FAILED                                [ 50%]
test_pytest_sample.py::test_answer1 PASSED                               [100%]

=================================== FAILURES ===================================
_________________________________ test_answer __________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_pytest_sample.py:39: AssertionError
=========================== short test summary info ============================
FAILED test_pytest_sample.py::test_answer - assert 4 == 5
========================= 1 failed, 1 passed in 0.04s ==========================
(venv) [18:22:12][~/project/TestTech/pycharm_test_env/testcases]$ 

(venv) [18:23:56][~/project/TestTech/pycharm_test_env/testcases]$ pytest -k test_b
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases
collected 13 items / 12 deselected / 1 selected                                

test_pytest_sample.py .                                                  [100%]

======================= 1 passed, 12 deselected in 0.02s =======================
(venv) [18:26:58][~/project/TestTech/pycharm_test_env/testcases]$ pytest -k test_b -v
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases
collected 13 items / 12 deselected / 1 selected                                

test_pytest_sample.py::TestDemo::test_b PASSED                           [100%]

======================= 1 passed, 12 deselected in 0.02s =======================
(venv) [18:27:08][~/project/TestTech/pycharm_test_env/testcases]$ pytest -k 'test_b or test_a' -v
============================= test session starts ==============================
platform darwin -- Python 3.8.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fengsonglin/project/TestTech/pycharm_test_env/testcases
collected 13 items / 8 deselected / 5 selected                                 

test_pytest_sample.py::TestDemo::test_a PASSED                           [ 20%]
test_pytest_sample.py::TestDemo::test_b PASSED                           [ 40%]
test_pytest_sample.py::test_answer FAILED                                [ 60%]
test_pytest_sample.py::test_answer1 PASSED                               [ 80%]
test_unittest.py::TestStringMethods::test_abc PASSED                     [100%]

=================================== FAILURES ===================================
_________________________________ test_answer __________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_pytest_sample.py:72: AssertionError
=========================== short test summary info ============================
FAILED test_pytest_sample.py::test_answer - assert 4 == 5
================== 1 failed, 4 passed, 8 deselected in 0.06s ===================
(venv) [18:27:22][~/project/TestTech/pycharm_test_env/testcases]$ 
"""
#上面是命令行


#下面是pychar 操作
@pytest.fixture()
def login():
    username = "jerry"
    return username


class TestDemo:
    #调用test_a的时候会调用登录
    def test_a(self,login):
        print(f"test_a username= {login}")

    def test_b(self):
        print("test_b")

    def test_c(self,login):
        print(f"test_c login = {login}")

def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (20,22)
])

def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

if __name__ == '__main__':
    pytest.main(['test_pytest_sample.py::TestDemo','-v'])