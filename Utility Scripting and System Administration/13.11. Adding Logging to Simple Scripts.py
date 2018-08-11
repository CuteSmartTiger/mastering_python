# 13.11. Adding Logging to Simple Scripts
# 日志官方文档：https://docs.python.org/3/howto/logging-cookbook.html


import logging
def main():
    # Configure the logging system
    # filename指定日志文件，通过basicconfig过滤日志级别
    # 想要你的日志消息写到标准错误中，而不是日志文件中，logging.
    # basicConfig(level=logging.INFO)
    logging.basicConfig(filename='app.log',level=logging.ERROR)
    # logging.basicConfig(filename='app.log', level=logging.WARNING, format='%(levelname)s:%(asctime)s:%(message)s')
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()

# 在本文件所在的当前目录下新建了一个app.log
# 运行此文件时 日志相关信息输入到app.log中
# 输出为：
# CRITICAL:root:Host www.python.org unknown
# ERROR:root:Couldn't find 'spam'

# 注：The five logging calls (critical(), error(), warning(), info(), debug()) represent
# different severity levels in decreasing order.


# basicConfig() 在程序中只能被执行一次。想改变日志配置，
# 需先获取 root logger ，然后直接修改它。
# logging.getLogger().level = logging.DEBUG



# 如果想在配置文件中定义这些信息 则可以写如下 ：
import logging
import logging.config
def main():
    # Configure the logging system
    # 将配置文件中的文件名 日志级别等信息导入
    logging.config.fileConfig('logconfig.ini')