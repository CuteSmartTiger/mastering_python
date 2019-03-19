# -*- encoding: utf-8 -*-
# @Time    : 2019/3/18 16:56
# @Author  : liuhu
# @File    : 配置日志.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import logging


# LOG_FORMAT = "%(asctime)s - %(levelname)s-%(name)s:%(message)s"
LOG_FORMAT = '[%(asctime)s: %(levelname)s in %(pathname)s:%(lineno)05d]: %(message)s '
logging.basicConfig(filename='vdimonitor.log', level=logging.DEBUG, format=LOG_FORMAT)
def test_log():
    try:
        1/0
    except ZeroDivisionError as e:
        logging.debug('test',exc_info = True)
    else:
        print '测试日志'
test_log()

