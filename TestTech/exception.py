#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:05
"""

try:
    num1 = int(input("输入一个除数"))
    num2 = int(input("输入一个被除数"))
    print(num1/num2)
except ZeroDivisionError:
    print("被除数不能为0")
except ValueError:
    print("输入的需要时数值型整数")
except:
    print("这是一个通用型异常")
else:
    print("没有发生异常")
finally:
    print("无论发没发生异常，都执行")

