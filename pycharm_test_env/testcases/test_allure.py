#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/20 21:30
"""

#allure 介绍
"""
allure 是一个轻量级，灵活的，支持多语言的测试报告工具；
多平台的，奢华的report框架
可以为dev/qa提供详尽的测试报告、测试步骤
也可以为管理层提供high leve统计报告
Java语言开发的，支持pytest，JavaScrpit，PHP，ruby等
可以集成到jenkins
"""
#allure安装
"""
https://github.com/allure-framework/allure2/releases
windows、mac 通用安装方法(如果下面的失效使用这个https://scoop.sh/#/apps?q=allure&s=0&d=1&o=true)
- https://githubcom/allure-framework/allure2/release下载allure2.7.zip包
- 解压->进入bin目录->运行allure.bat
- 把bin目录加入PATH环境变量
Mac 可以使用brew 安装
brew install allure
官网:http://allure.qatools.ru/
文档:https://docs.qameta.io/allure/#
"""

#pytest allure 搭配使用
"""
文档：https://docs.qameta.io/allure/#_pytest

- 安装allure-pytest插件
- pytest xxx.py --alluredir=/tmp/my_allure_results
pytest [测试文件] -s -q --alluredir=./result/(--alluredir这个
选项用于指定存储测试结果的路径)
- allure serve /tmp/my_allure_results
查看测试报告，上面的命令执行完毕之后，会直接打开默认浏览器展示当前报告

上面执行完成
http://127.0.0.1:57244/index.html

如果从结果生成报告，这是一个启动tomcat的服务，需要两个步骤
- 生成报告
allure generate ./result/ -o ./report/ --clean
(覆盖路径加--clean)
- 打开报告
allure open -h 127.0.0.1 -p 8883 ./report/

"""
import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


