# 10.13 安装私有的包

# 目的：为自己导入的特定的包

# 在sys.path中用户的“site-packages”目录位于系统的“site-packages”
# 目录之前。 因此，你安装在里面的包就比系统已安装的包优先级高

# pip install --user packagename


# 10.15 分发包
# 目的：如何让编写的完成的程序发布出去，以便他人下载安装
# setup.py 和 MANIFEST.in 文件放在你的包的最顶级目录

# 示例：一个常见错误就是仅仅只列出一个包的最顶级目录，忘记了包含包的子组件
# setup.py
from distutils.core import setup
setup(name='projectname',
    version='1.0',
    author='Your Name',
    author_email='you@youraddress.com',
    url='http://www.you.com/projectname',
    packages=['projectname', 'projectname.utils'],
)


# # MANIFEST.in    列出所有在你的包中需要包含进来的非源码文件
# include *.txt
# recursive-include examples *
# recursive-include Doc *