#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/18 22:43
"""
# time 模块常用的方法
"""
time.asctime() 国外的时间格式
time.time() 时间戳
time.sleep() 等待
time.localtime() 时间戳转成时间元祖
time.starttime() 将当前的时间戳转成带格式的时间
- 格式: time.strftime("%Y%m%d %H-%M-%S",time.lcaltime())
"""

import  time

#Fri Nov 18 22:45:23 2022
print(time.asctime())
#1668782723.520384
print(time.time())
#time.struct_time(tm_year=2022, tm_mon=11, tm_mday=18, tm_hour=22, tm_min=45, tm_sec=23, tm_wday=4, tm_yday=322, tm_isdst=0)
print(time.localtime())
#2022-11-18 22-47-30
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

#获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60 * 60 *24 * 2
time_tuple = time.localtime(two_day_before)
#2022-11-16 22-49-27
print(time.strftime("%Y-%m-%d %H-%M-%S", time_tuple))