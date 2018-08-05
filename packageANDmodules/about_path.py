import sys
print(sys.path)
# 知识点一：模块优先导入顺序：
# 当前目录路径
# 虚拟环境路径
# site-packages

# 第一次导入模块与第二次导入模块的区别
# 第一次导入后运行时执行模块里的函数，并将名称存储，第二次导入时，直接调用


# import test_for_path

# 使用from B import C   ,B为模块，C为方法,B中的顶级方法也会执行，这点需要注意
from test_for_path import come2
print(come2())


# 查看当前导入模块数量
print(sys.modules)

import site



# 知识点二：添加路径的方法
# 一则在当前路径列表中添加
# 二则在当前用户环境变量中添加
# 三则在sys.path中新建pth结尾的文件，在文件中加入路径

