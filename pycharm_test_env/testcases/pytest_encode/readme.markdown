### 打包需要两个工具
wheel,setuptools

在打包之前可以先到test目录下的test_encode.py执行测试
看看中文是否显示乱码

### 步骤一
```
(venv) [11:05:11][~/project/TestTech/pycharm_test_env/testcases/pytest_encode]$ python3.8 setup.py sdist bdist_wheel
running sdist
running egg_info
writing manifest file 'pytest_encode.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
creating pytest_encode-1.0
creating pytest_encode-1.0/pytest_encode
creating pytest_encode-1.0/pytest_encode.egg-info
creating pytest_encode-1.0/test
copying setup.py -> pytest_encode-1.0
copying pytest_encode/__init__.py -> pytest_encode-1.0/pytest_encode
copying pytest_encode.egg-info/PKG-INFO -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/SOURCES.txt -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/dependency_links.txt -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/entry_points.txt -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/not-zip-safe -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/requires.txt -> pytest_encode-1.0/pytest_encode.egg-info
copying pytest_encode.egg-info/top_level.txt -> pytest_encode-1.0/pytest_encode.egg-info
copying test/test_encode.py -> pytest_encode-1.0/test
creating dist
Creating tar archive
removing 'pytest_encode-1.0' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/pytest_encode
copying pytest_encode/__init__.py -> build/lib/pytest_encode
/Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
running install
running install_lib
creating build/bdist.macosx-10.14-x86_64
creating build/bdist.macosx-10.14-x86_64/wheel
creating build/bdist.macosx-10.14-x86_64/wheel/pytest_encode
running install_egg_info
Copying pytest_encode.egg-info to build/bdist.macosx-10.14-x86_64/wheel/pytest_encode-1.0-py3.8.egg-info
running install_scripts

```

###dist
```
1.tar.gz 源码包
2.whl 可以通过pip install
(venv) [11:05:13][~/project/TestTech/pycharm_test_env/testcases/pytest_encode]$ pip install dist/pytest_encode-1.0-py3-none-any.whl 
Processing ./dist/pytest_encode-1.0-py3-none-any.whl
Requirement already satisfied: pytest in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest-encode==1.0) (7.2.0)
Requirement already satisfied: attrs>=19.2.0 in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (22.1.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (1.0.4)
Requirement already satisfied: iniconfig in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (1.1.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (1.0.0)
Requirement already satisfied: packaging in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (21.3)
Requirement already satisfied: tomli>=1.0.0 in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from pytest->pytest-encode==1.0) (2.0.1)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/fengsonglin/project/TestTech/pycharm_test_env/venv/lib/python3.8/site-packages (from packaging->pytest->pytest-encode==1.0) (3.0.9)
Installing collected packages: pytest-encode
Successfully installed pytest-encode-1.0
(venv) [11:07:10][~/project/TestTech/pycharm_test_env/testcases/pytest_encode]$ 


```

执行完成之后，再次到test中执行test_encode.py,看看是否已经变回了中文