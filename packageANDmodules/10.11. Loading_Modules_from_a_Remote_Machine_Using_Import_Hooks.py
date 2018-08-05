# 10.11. Loading Modules from a Remote Machine UsingImport Hooks
# 目的：常用的是本地导入模块，本节知识讲的主要是通过钩子函数从远程导入模块

# 本章知识学习待定

# 3.4版本后已不支持imp
import importlib
import urllib.request
import sys


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url,imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


# print(sys.modules)