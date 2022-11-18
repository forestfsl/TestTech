#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 17:57
"""

#文件读取
#def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
"""
参数说明:
- name: 文件名称的字符串值
- model: 只读r,写入w，追加a，默认文件访问模式为只读(r).b:二进制模式,x:create file
- bufferring:寄存区缓存 0代表不寄存，1访问文件的时候会寄存 
>1寄存区的缓冲区大小，负值代表寄存区的缓冲大小则为系统默认
"""
"""
<_io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>
"""
print(open('data.txt'))

f = open('data.txt')

"""
True
"""
print(f.readable())
"""
a
"""
#print(f.readline())
"""
['b\n', 'c\n', 'd\n', 'e\n', 'f\n', 'g']
"""
print(f.readlines())
f.close()

"""
['a\n', 'b\n', 'c\n', 'd\n', 'e\n', 'f\n', 'g']
"""
with open('data.txt') as f1:
    print(f1.readlines())
#f1.close() 不需要关闭，因为with语句块在文件打开，操作完毕之后，会自动关闭


"""
a

b

c

d

e

f

g
有两次换行的原因是因为data.txt 中已经有一次换行的操作，然后print本身自己也会有一次
"""
# 图片读取需要使用rb open('data.txt','rb') 读取二进制格式
#正常的文本，rt是默认格式
with open('data.txt') as f1:
    while True:
        line = f1.readline()
        if line:
             print(line)
        else:
            break

"""
read() 读取文件中的所有内容(缺点:当文件内容非常强大，大于内存时候，无法使用这个方法)
readable() 判断文件是否可读
readline() 每次读取一行(包括行结束符),返回的是一个字符串对象，保存当前行内存
readlines() 读取所有行的内容，放到列表中
"""

#如何使用JSON
#import json
#常用的几种方法
"""
json.dumps(python_obj)把数据类型转成字符串
json.loads(json_string)把字符串转成json
json.dump()把数据类型转换成字符串并存储在文件中
json.load(file_stream)把文件打开，把里面的字符转换成数据类型
"""
