# 10.2. Controlling The Import of Everything
from test import *

# 导入失败
import test

print(name3)
print(come3())

# __all__ = ["come2","name3","come3"]


# 10.3. Importing Package Submodules Using Relative Names

# mypackage/
#     __init__.py
#     A/
#         __init__.py
#         spam.py
#         grok.py
#     B/
#         __init__.py
#         bar.py


# 相对导入看起来像是浏览文件系统，但是不能到定义包的目录之外
# mypackage/A/spam.py
# from . import grok
# 如果模块mypackage.A.spam要导入不同目录下的模块B.bar，它应该使用的import语句如下：
# mypackage/A/spam.py
# from ..B import bar
# 指定目录名.为当前目录，..B为目录../B。这种语法只适用于import

from mypackage.A import grok  # OK
from . import grok             # OK
import grok                    # Error (not found)

# 更多的包的相对导入的背景知识,请看 PEP 328

# 10.5 利用命名空间导入目录分散的代码
import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok