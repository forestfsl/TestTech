#系统内置模块

import sys

"""
/usr/bin/python3 /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 49946 --file /Users/fengsonglin/project/TestTech/TestTech/module.py 
Connected to pydev debugger (build 222.4345.23)
['/Users/fengsonglin/project/TestTech/TestTech', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/third_party/thriftpy', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', '/Users/fengsonglin/project/TestTech', '/Users/fengsonglin/Library/Caches/JetBrains/PyCharmCE2022.2/cythonExtensions', '/Users/fengsonglin/project/TestTech/TestTech', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages']

Process finished with exit code 0

"""
print(sys.path)

import os
import re
import json
import time

# 第三方開源模块 需要使用[17:23:40][~]$ pip3 install yaml 模块安装
import  yaml
import requests

# 引入自定义模块
from baidu import search,search1
from baidu import hello
from baidu import SearchDemo
"""
如果太多的话，可以直接用下面这个导入方式
"""
#from baidu import  *
search()
print(hello)
print(SearchDemo())

#常用方法

"""
找出当前模块定义的对象
找出参数模块定义的对象
"""
"""
['SearchDemo', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hello', 'json', 'os', 're', 'requests', 'search', 'search1', 'sys', 'time', 'yaml']
"""
print(dir())
"""
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']

"""
print(dir(sys))
"""
['/Users/fengsonglin/project/TestTech/TestTech', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/third_party/thriftpy', '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', '/Users/fengsonglin/project/TestTech', '/Users/fengsonglin/Library/Caches/JetBrains/PyCharmCE2022.2/cythonExtensions', '/Users/fengsonglin/project/TestTech/TestTech', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Users/fengsonglin/Library/Python/3.8/lib/python/site-packages', '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages', '/Library/Python/3.8/site-packages']
"""
#模块的查找路径，当出现调用函数不是进入想要的模块函数时候，可能就是因为存在同名函数
print(sys.path)
"""
Python 解析器对模块位置的搜索顺序是：
- 包含输入脚本的目录(如果未指定文件，则为当前目录)
- PYTHONPATH（目录名称列表，语法与shell的PATH变量相同）
- 安装的默认路径
"""
