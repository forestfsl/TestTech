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