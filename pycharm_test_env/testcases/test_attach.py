#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/21 23:02
"""
import allure
import pytest

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/Users/fengsonglin/project/TestTech/pycharm_test_env/testcases/resources/com.apple.dt.Xcode.png",name="这是一个图片",attachment_type=allure.attachment_type.PNG)