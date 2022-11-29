#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/27 22:04
"""
"""
ActionChains 用法二：鼠标移动到某个元素
action = ActionChains(self.driver)
action.move_to_element(element)
action.perform()
"""

"""
ActionChains 用法三：拖拽
click_and_hold
"""

"""
ActionChains 用法四:模拟按键方法
模拟按键有很多种方法：能用win32api来实现，能用SendKeys来实现，也可以
用selenium的WebElement对象的send_keys()方法来实现，这里ActionChains
类也提供了几个模拟按键的方法
用法：
Action = ActionChains(driver)
action.send_keys(Keys.BACK_SPACE)
或者
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)   
action.perform()
"""

"""
TouchAction
Document:https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.touch_actions.html
https://www.selenium.dev/selenium/docs/api/dotnet/html/T_OpenQA_Selenium_Interactions_TouchActions.htm
https://support.smartbear.com/crossbrowsertesting/docs/automated-testing/frameworks/selenium/about/selenium-touchactions.html
类似于ActionChains，ActionChains只是针对PC端程序鼠标模拟的一些列操作，对H5页面操作时无效的，TouchAction可以对h5页面操作，通过TouchAction
可以实现点击、拖拽、读点触控、与及模拟手势的各种操作
- 手势控制
tap:指定元素伤敲击
double_tap-在指定元素上双敲击
tap_and_hold 在指定元素伤点击但不释放
move:手势移动并滚动
release：释放手势
scroll：手势点击并滚动
scroll_from_element：从某个元素位置开始手势点击并滚动(向下为负数，向上为正数)
long_press:长按元素
flick:手势滑动
flick_element:从某个元素位置开始手势滑动
Perform 执行
"""