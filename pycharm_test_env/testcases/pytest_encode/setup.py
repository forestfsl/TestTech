#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/26 10:48
"""
from setuptools import setup

setup(
    name='pytest_encode',
    url='https://githubcom/forestfsl/pytest-encode',
    version='1.0',
    author='forest',
    author_email='438864519@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize()',
    classifiers=[#分类缩影，pip所属包的分类
        'Framework::Pytest',
        'Programming Language::Python',
        'Topic::Software Development::Testing',
        'Programming Language::Python::3.0',
     ],
    license='proprietary',
    packages=['pytest_encode'],
    keywords=[
        'pytest','py.test','pytest_encode',
    ],
    #需要安装的依赖
    install_requires=[
        'pytest'
    ],
    #入口模块，或者入口函数
    entry_points={
        'pytest11':[
            'pytest-encode = pytest_encode',
        ]
    },
    zip_safe=False
)
