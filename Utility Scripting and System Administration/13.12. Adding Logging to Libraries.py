# 13.12. Adding Logging to Libraries

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# 如果缺少这句配置，则日志无输出
# logging.basicConfig()   #CRITICAL:__main__:A Critical Error!
logging.basicConfig(level=logging.ERROR)   #CRITICAL:__main__:A Critical Error!


# logging.getLogger('filename.py').level=logging.DEBUG    这句话可以
# 在python解释器运行中对配置信息进行更改，这样可以针对的文件进行修改

# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')

if __name__ == "__main__":
    func()

