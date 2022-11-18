#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:50
"""
#urllib 库
"""
python2
- import urllib2
- response = urllib.urlopen("http://www.baidu.com")

python3
- import urllib.request
- response = urllib.request.urlopen("http://www.baidu.com")

"""
import  urllib.request

response: object = urllib.request.urlopen("http://www.baidu.com")
print("response.read \n")
#可以看到输出一堆东西
print(response.read())
