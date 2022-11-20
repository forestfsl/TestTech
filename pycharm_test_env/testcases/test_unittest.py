#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 11:37
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp 方法级别")

    def tearDown(self) -> None:
         print("tearDown 方法级别")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
            print("tearDownClass")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_abc(selfs):
        print('test abc')

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断1==1")
    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1,2,"判断1！=2")

if __name__ == '__main__':
    #执行方法一:
    unittest.main()


"""
Unittest 提供了test cases、test suites、test fixtures、test runner等
编写规范
- 测试模块首先import unittest
- 测试类必须继承unittest.TestCase
- 测试方法必须以test_开头

总结：
setUp 用来为测试准备环境，tearDown用来清理环境
如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们
可以使用setUpClass()和tearDownClass(),比如数据库的连接与销毁
- 如果想有些方法不在本次执行，使用@unittest.skip

多个测试用例的集合就是测试套件、通过测试套件来管理多个测试用例
- 执行方法一：unittest.main()
- 执行方法二:加入容器中执行
suite=unittest.TestSuite()
suite.addTest(TestMethod("test_01"))
suite.addTest(TestMethod("test_02"))
unittest.TextTestRunner().run(suite)

#执行方法三：执行某个测试类
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
suite = unittest.TestSuite([suite1,suite2])
unittest.TextTestRunner(verbosity=2).run(suite)

#执行方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
- discover可以一次调用多个脚本
- test_dir 被测试脚本的路径
- pattern 脚本名称的匹配规则
"""