#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 18:12
"""

#命令行操控字面量
"""
[17:59:09][~/project/TestTech]$ python3
Python 3.8.9 (default, May 17 2022, 12:55:41) 
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("my name is songlin")
my name is songlin
>>> name='hello'
>>> print('my name is %s '%name)
my name is hello 
>> age = 3
>>> print('my name is %s,my age is %d '%(name,age))
my name is hello,my age is 3 
>>> 
>>> print('my name is %s,my age is %d，num is %f' %(name,age,3.1415926))
my name is hello,my age is 3，num is 3.141593

>>> print('my name is {}'.format(name))
my name is hello
"""

name = 'songlin'
age = 20
"""
my name is songlin, age is 20
"""
print('my name is {}, age is {}'.format(name,age))
"""
my name is songlin, age is 20,songlin2020songlin
"""
print('my name is {0}, age is {1},{0}{1}{1}{0}'.format(name,age))

list = [1,3,4]
dict = {'name':'tom','gender':'male'}
"""
my list is [1, 3, 4], dict is {'name': 'tom', 'gender': 'male'}
"""
print('my list is {}, dict is {}'.format(list,dict))

namelist = ['lili','tom','jerry']
"""
we name:lili、tom and jerry
"""
print('we name:{}、{} and {}'.format(*namelist))

"""
my name is:tom、gender is male
"""
print('my name is:{name},gender is {gender}'.format(**dict))

"""
my name is {name},age is {age}
"""
print('my name is {name},age is {age}')
"""
my name is songlin,age is 20
"""
print(f'my name is {name},age is {age}')

"""
my name is songlin,age is 20,my list is [1, 3, 4],my dict is {'name': 'tom', 'gender': 'male'}

"""
print(f'my name is {name},age is {age},my list is {list},my dict is {dict}')
"""
my name is songlin,age is 20,my list is 1,my dict is tom

"""
print(f"my name is {name},age is {age},my list is {list[0]},my dict is {dict['name']}")

"""
my name is SONGLIN
"""
print(f"my name is {name.upper()}")

"""
result is 3
"""
print(f'result is {(lambda x:x+1)(2)}')


