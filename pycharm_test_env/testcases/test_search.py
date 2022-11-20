#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 11:53
"""
import unittest


#被测试的方法
class Search:
    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search3")
        # search = Search()
        assert True == self.search.search_fun()

"""
(venv) [12:50:57][~/project/TestTech/pycharm_test_env]$ python3 test_search.py
setUpClass
test_search1
search
.test_search2
search
.tearDownClass

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""
if __name__ == '__main__':
    #执行方法一:执行当前文件所有的unittest
    #unittest.main()
    #执行方法二：执行指定的测试用例(如果在pycharm中执行不成功的话，可以在命令行中执行)
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search2"))
    # unittest.TextTestRunner().run(suite)
    #执行方法三：执行某个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)