# 13.7. Copying or Moving Files and Directories
# https://docs.python.org/3/library/shutil.html
import shutil
# Copy src to dst. (cp src dst)
# shutil.copy(src, dst)
shutil.copy(r'C:\liuhu\note\documents\mastering python\README.md',r'C:\liuhu\note\documents\mastering python\packageANDmodules')

# # Copy files, but preserve metadata (cp -p src dst)
# shutil.copy2(src, dst)
# shutil.copy2(r'C:\liuhu\note\documents\mastering python\Utility Scripting and System Administration',r'C:\liuhu\note\documents\mastering python\packageANDmodules')

# # Copy directory tree (cp -R src dst)
# shutil.copytree(src, dst)
# dst目录不可以与现有的冲突，否则无法复制，若dst不存在，则复制时会创建一个目录
shutil.copytree(r'C:\liuhu\note\documents\mastering python\Utility Scripting and System Administration',r'C:\liuhu\note\documents\mastering python\xxx')


# # Move src to dst (mv src dst)
# shutil.move(src, dst)
#
# # 软连接的操作
# # If you want to copy the symbolic link instead, supply the follow
# # _symlinks keywordargument like this:
#
# shutil.copy2(src, dst, follow_symlinks=False)
#
# # If you want to preserve symbolic links in copied directories, do this:
# shutil.copytree(src, dst, symlinks=True)
#
#
#
# # 忽略特定的文件
# def ignore_pyc_files(dirname, filenames):
#     return [name in filenames if name.endswith('.pyc')]
# shutil.copytree(src, dst, ignore=ignore_pyc_files)
#
# # 或者使用已有的函数
# shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*.pyc'))


# copymode( src, dst)	 只是会复制其权限其他的东西是不会被复制的
# copystat( src, dst)	 复制权限、最后访问时间、最后修改时间