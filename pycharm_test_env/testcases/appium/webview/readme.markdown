#### 查看手机browser
[21:52:13][~/project/HLLCourseLive]$ adb shell pm list package | grep browser
package:com.android.browser

#### 查看browser版本
[21:52:22][~/project/HLLCourseLive]$ adb shell pm dump com.android.browser | grep version
      versionCode=23 targetSdk=23
      versionName=6.0.1

#### 测试过程中遇到的问题
- 1.No Chromedriver found that can automate Chrome '66.0.3359'
> 解决方法
1.[Appium自动化测试遇到的chromedriver/chrome坑](http://t.zoukankan.com/fengye151-p-12901176.html)

2.[appium自动化webview时遇到的chromedriver问题](https://www.likecs.com/show-308501028.html#sc=43)

3.[chromedriver version](https://chromedriver.storage.googleapis.com/index.html)

启动的时候可以按照2来启动，或者命令行直接指定
'chromedriverExecutable': '/Users/fengsonglin/Documents/chromedriver'


如果没有指定chromedriver的话，会自动去到默认路径寻找
/Applications/Appium Server GUI.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac


# 过滤http链接
终端中输入:
adb logcat -v time | grep http


如果在chrome://inspect/#devices 看不到app页面，说明webview的开关没有开启