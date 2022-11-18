#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:18
"""
#通过class关键字定义一个类
#self 访问的变量就是实例变量
class Person:
    name = "defalut"
    age = 0
    gender = 'male'
    weight = 0

# 初始化的时候调用
    def __init__(self,name,age,gender,weight):
        print("init")
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def set_param(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age
    def eat(self):
        print(f"{self.name}eating")

    def play(self):
        print(f"{self.name}playing")

    def jump(self):
        print(f"{self.name}jump")

    @classmethod
    def test(cls):
        print("测试类方法")
"""
类可以访问变量是因为传递进去的时候会转换成实例对象，但是直接访问
方法不行，因为访问方法的时候不会转成实例对象
如果需要访问方法，必须声明为类方法@classmethod
"""
#类变量 defalut
print(Person.name)
Person.name = "ece"
#ece
print(Person.name)
#测试类方法
print(Person.test())


zs = Person("songlin",20,'man',160)
zs.name = "zhangsan"
print("名字:",zs.name)
zs.set_param("lisi")
print("名字:",zs.name)
zs.age = 20
print("age:",zs.age)
zs.set_age(32)
print("age:",zs.age)
zs.weight = 160
print("weight:",zs.weight)

zs.jump()
zs.eat()
zs.play()

songlin = Person("songlin",20,'man',160)
songlin.jump()
songlin.eat()
songlin.play()
"""
以上的输出为
名字: zhangsan
名字: lisi
age: 20
age: 32
weight: 160
"""
