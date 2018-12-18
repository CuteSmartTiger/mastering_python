#!/usr/bin/env python
# -*- coding: utf-8 -*-
# semaphore 控制每次允许的最大并发线程数
# 线程池同样可以实现这个效果

# 使用场景：
# 1.比如文件的写入，单次并发最大线程数为1

# 本节需要掌握的知识点
# queue中的Queue

import threading
import time


class SpiderConsumer(threading.Thread):
    def __init__(self, url, name, sema):
        super().__init__(name=name)
        self.url = url
        self.sema = sema

    # 这里重写了父类中的run方法
    def run(self):
        time.sleep(1)
        print('#{0}'.format(self.name), '当前页面爬取成功')
        # 爬取成功一次释放一次锁，通过看源码
        # 可知，释放一次，则value加1，锁全部
        # 释放，Semaphore中使用了Condition实现同步
        self.sema.release()


class UrlProducer(threading.Thread):
    def __init__(self, sema):
        self.sema = sema
        super().__init__(name='url produce')

    # 这里重写了父类中的run方法
    def run(self):
        for i in range(15):
            url = 'www.baidu.com/{0}/'.format(i)
            # 获取锁，锁住五个线程，当value值为0时，
            # 释放锁，然后重新开辟五个线程
            # 每执行一次acquire，sema中的value值减小1,
            # value等于0零时调用wait方法，然后阻塞
            self.sema.acquire()
            spider = SpiderConsumer(url, i, self.sema)
            spider.start()


if __name__ == '__main__':
    # 单次允许的最大开辟的线程
    sema = threading.Semaphore(value=4)
    url_producer = UrlProducer(sema)
    url_producer.start()
