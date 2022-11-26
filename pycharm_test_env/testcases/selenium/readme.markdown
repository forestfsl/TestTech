#Driver 的介绍
https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

#Driver 的下载
- 淘宝镜像：https://npm.taobao.org/mirrors/chromedriver/
- 官方网站:https://chromedriver.storage.googleapis.com/index.html

#Driver 的安装
- 找到和自己浏览器版本适配的driver版本(google浏览器右上角->帮助->关于谷歌 会看到有个版本信息，比如说我的是Version 107.0.5304.110)
- 导入到开发环境变量中

selenium 的文档入门
https://selenium-python.readthedocs.io/



# 显式等待、隐式等待
```
元素受到网络影响，有时候慢，有时候快，但是这样有一个很不好的效果，就是有时候
网络快，也是需要等到这么久

```
- 强制等待，现成休眠一定时间
time.sleep(3)

```
全局生效

```
- 设置一个等待时间、轮训查找（默认0.5）元素是否出现,如果没出现就显示异常
self.driver.implicity_wait(3)

- 显式等待
在代码中定义等待条件，当条件发生时才继续执行代码，WebDriverWait
撇和until()和unitil_not()方法，根据判断条件进行等待，程序每隔一段时间(默认0.5秒)
进行条件判断，如果条件成立，则执行下一步，否则继续等待，知道超过设置最长的时间
