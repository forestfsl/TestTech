### appium 环境安装
- 安装SDK
1.下载sdk Android studio 地址https://developer.android.com/studio/index.html
2.中文官网下载地址:http://tools.android-studio.org/index.php/sdk
- 安装SDK
其实sdk就是个文件夹，下载之后需要手动更新，配上环境变了就可以使用，不需要手动安装
- 配置android SDK 环境变量如下:
ANDROID_HOME D:\ADT-BUNDLE-MAC-X86-64-20140702\sdk
PATH %ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools
- 检查是否安装成功 cmd
adb 回车或者adb shell

- 安装appium desktop(appium server + appium inspector 工具)
1.下载对应的操作系统安装包:https://github.com/appium/appium-desktop/releases
2.如果不需要appium inspector,也可以通过npm 直接安装appium
```
官方安装(不推荐)
npm install -g appium
淘宝提供(推荐)
npm install -g cnpm -registry=https://registry.npm.taobao.org
cnpm install -g appium

运行
appium 不报错说明成功
```

- 安装appium python client
1.方式一：pip install appium-python-client(推荐)
2.方式2:下载源码包
下载地址:https://github.com/appium/python-client
https://pypi,python.org/pypi/Appium-Python-Client
解压后在命令行中进入python-client-master目录，该目录下包含setup.py文件
执行python setup.py install 命令安装客户端


- 安装appium-doctor 检测appium的安装环境
npm install -g cnpm -registry=https://registry.npm.taobao.org
cnpm -g install appium-doctor
- 在命令行执行appium-doctor
