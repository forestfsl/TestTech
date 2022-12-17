#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/12/10 11:03
"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestDw():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '6.0'
        desire_caps['deviceName'] = 'emulator-5554'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = '.mainnesting.view.MainNestingActivity'
        desire_caps['noReset'] = "true"
        desire_caps['unicodeKeyBoard'] ="true"
        desire_caps['resetKeyBoard'] = "true"
        # 首次启动不停止app
        desire_caps['dontStopAppOnReset'] = "true"
        desire_caps['skipDeviceInitialzation'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1.打开雪球app
        2.点击搜索框
        3.向搜索框里面输入阿里巴巴
        4.在搜索结果里选择阿里巴巴，然后进行点击(appium inspector 通过xpath获取//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']，因为通过id获取有多个元素)
        5.获取 阿里巴巴的股价，并判断这只股价的价格>90
        如果是android 可以考虑用
        [18:49:57][~/project/TestTech]$ which uiautomatorviewer
/Users/fengsonglin/android-sdk-macosx/tools/uiautomatorviewer
        """
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(by=By.XPATH,value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        """
        这里当前价格为什么不通过android.widget.TextView 来定义i，是因为这个地方有多处调用
        """
        current_price = float(self.driver.find_element(by=By.ID,value="com.xueqiu.android:id/current_price_dtv").text)
        expect_price = 170
        #assert_that(current_price, close_to(expect_price,expect_price * 0.1))

        assert current_price > 90

        sleep(3)

    @pytest.mark.skip
    def test_attr(self):
        """
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入:alibaba
        判断【阿里巴巴】是否课件
        如果课件 打印搜索成功，如果不可见，打印搜索失败
        appium-uiautomator2-server 源码
        :return:
        """
        element = self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element(by=By.XPATH, value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            print(alibaba_element.get_attribute("displayed"))
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    @pytest.mark.skip
    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        sleep(4)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()


    """
    //*[@resource-id='com.xueqiu.android:id/title_container']/	
android.widget.FrameLayout[2] 股票标签的xpath
    """

    @pytest.mark.skip
    def test_get_current(self):
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(by=By.XPATH,value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        """
        #这样会找不到，因为是孙子节点，所以要用下面那种形式，加多一个/代表使用相对路径
//*[@text="09988"]/../../*[@resource-id='com.xueqiu.android:id/current_price_dtv']

//*[@text="09988"]/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']
        """
        current_price = self.driver.find_element(by=By.XPATH,value="//*[@text='09988']/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']").text
        print(f"当前09988 对应的股价价格是:{current_price}")
        assert float(current_price) > 90

    @pytest.mark.skip
    def test_myinfo(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入到登录页面
        3.输入用户名，输入密码
        4.点击登录
        :return:
        """
        #这里要是text 包含我的，有多个地方出现，那么久回定义不到，这个时候，我们就可以考虑采取使用resourceId，结合text处理
        # self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR,value='new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("我的")').click()
        #sleep(5)
        self.driver.find_element(by=By.ID,value="com.xueqiu.android:id/profile_name").click()
        #sleep(5)
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR,value='new UiSelector().textContains("我的主页")').click()
        sleep(5)
        """
        uiautomator 定位
        - 父子关系定位 childSelector
        有时候不能直接定位某个元素，但是它的父元素很好定位，这时候就先定位父元素，通过父元素找儿子
        son = 'resourceId("com.baidu.yuedu:id/rl_tabs").childSelector(tex("股票"))
        - 兄弟定位fromParent
        有时候父元素不好定位，当时跟它相邻的兄弟元素很好定位，这时候就可以通过兄弟元素，找到同一父级元素下的子元素
        brther='resourceId("com.baidu.yuedu:id/lefttitle").fromParent(text("用户"))'
        """

    @pytest.mark.skip
    def test_scroll_find_element(self):
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("热门")').click()
        self.driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR,value='new UiScrollable(new UiSelector().'
                                                                       'scrollable(true).instance(0)).'
                                                                       'scrollIntoView(new UiSelector().text("明大教主").'
                                                                       ' instance(0));').click()
        sleep(5)

    #@pytest.mark.skip
    def test_get_current(self):
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(by=By.XPATH,value="//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        """
        #这样会找不到，因为是孙子节点，所以要用下面那种形式，加多一个/代表使用相对路径
    //*[@text="09988"]/../../*[@resource-id='com.xueqiu.android:id/current_price_dtv']

    //*[@text="09988"]/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']
            """
        locator = (By.XPATH,"//*[@text='09988']/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)

        # WebDriverWait(self.driver,10).until( lambda x: x.find_element(*locator)) 相当于上面两条语句叠加
        current_price = ele.text
        print(f"当前09988 对应的股价价格是:{current_price}")
        assert float(current_price) > 80

    @pytest.mark.skip
    def test_getattr(self):
        search_ele = self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))



if __name__ == '__main__':
    pytest.main()