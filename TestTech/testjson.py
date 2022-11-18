#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 19:18
"""
#json 由字典和列表组成


import  json
data = {
    "name":["jerry",'nickname'],
    "age":25,
    "gender":"female"
}

#<class 'dict'>
print(type(data))
data1 = json.dumps(data)
#{"name": ["jerry", "nickname"], "age": 25, "gender": "female"}
print(data1)
#<class 'str'>
print(type(data1))

data2 = json.loads(data1)
#<class 'dict'> 转换回来
print(type(data2))