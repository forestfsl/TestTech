#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:34
"""
""""
Python 标准库常见模块
操作系统相关:os
时间与日期:time datetime
科学计算：math
网络请求: urllib
"""
## os
"""
os模块主要对文件，目录的操作
- os.mkdir() 创建目录
- os.removedirs() 删除文件
- os.getcwd() 获取当前目录
- os.path.exists(dir or file)判断文件或者目录是否存在
"""
import os
#os.mkdir("os_test")
"""
['exception.py', 'list.py', 'randomDemo.py', 
'func_demo.py', 'testjson.py', 'classdemo.py', 
'syslibos_demo.py', 'module.py', 'venv', 'module.txt', 
'baidu.py', 'main.py', 'testChar.py', 'input-out.py', 
 'os_test', 'exception2.py', 'data.txt', '.idea']

"""
print(os.listdir("./"))

#os.removedirs('os_test')
#/Users/fengsonglin/project/TestTech/TestTech
print(os.getcwd())

#False
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt","w")
    f.write("hello ,os using")
    f.close()

