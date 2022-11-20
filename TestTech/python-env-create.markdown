##python 虚拟环境
- [x] 创建python3 -m venv tutorial-env
```commandline
[10:22:49][~/project/TestTech]$ python3 -m venv tutorial-env
[10:33:50][~/project/TestTech]$ ls
README.md	TestTech	tutorial-env
[10:33:51][~/project/TestTech]$ cd tutorial-env 
[10:34:19][~/project/TestTech/tutorial-env]$ ls
bin		include		lib		pyvenv.cfg
```
- [x] 进入虚拟环境
```commandline
[10:34:21][~/project/TestTech/tutorial-env]$ source bin/activate
(tutorial-env) [10:34:49][~/project/TestTech/tutorial-env]$ 
(tutorial-env) [10:34:49][~/project/TestTech/tutorial-env]$ pip list
Package    Version
---------- -------
pip        20.2.3
setuptools 49.2.1
WARNING: You are using pip version 20.2.3; however, version 22.3.1 is available.
You should consider upgrading via the '/Users/fengsonglin/project/TestTech/tutorial-env/bin/python3 -m pip install --upgrade pip' command.
```
- [x] 安装selenium
```commandline
tutorial-env) [10:36:16][~/project/TestTech/tutorial-env]$ pip install selenium==3.8.1
Collecting selenium==3.8.1
  Downloading selenium-3.8.1-py2.py3-none-any.whl (942 kB)
     |████████████████████████████████| 942 kB 229 kB/s 
Installing collected packages: selenium
Successfully installed selenium-3.8.1
WARNING: You are using pip version 20.2.3; however, version 22.3.1 is available.
You should consider upgrading via the '/Users/fengsonglin/project/TestTech/tutorial-env/bin/python3 -m pip install --upgrade pip' command.
```
- [x] 退出虚拟环境deactivate

从上面可以看到创建安装和退出，从命令行是比较麻烦的，所以通常我们是使用pycharm
来管理虚拟环境