# 13.8. Creating and Unpacking Archives

import shutil
# 解压缩
# shutil.unpack_archive('Python-3.3.0.tgz')

# 压缩名，压缩后缀，被压缩的目录，被压缩后的文件存放于被压缩目录下
# 注意：
# 1.地址路径必须加前缀r防止转义
# 2.路径如果换行，则查找时会出问题
shutil.make_archive('test','zip',r'C:\liuhu\note\documents\mastering python\Utility Scripting and System Administration')


print(shutil.get_archive_formats())
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"),
# ('tar', 'uncompressed tar file'), ('zip', 'ZIP file')]