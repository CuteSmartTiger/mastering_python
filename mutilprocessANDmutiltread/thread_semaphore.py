#!/usr/bin/env python
# -*- coding: utf-8 -*-
# semaphore 控制每次允许的最大并发线程

import threading
import time


class SpiderConsumer(threading.Thread):
    def __init__(self, url, name, sema):
        super().__init__(name=name)
        self.url = url
        self.sema = sema

    def run(self):
        time.sleep(1)
        print('#{0}'.format(self.name), '当前页面爬取成功')
        self.sema.release()


class UrlProducer(threading.Thread):
    def __init__(self, sema):
        self.sema = sema
        super().__init__(name='url produce')

    def run(self):
        for i in range(15):
            url = 'www.baidu.com/{0}/'.format(i)
            # 获取锁，锁住五个线程，当value值为0时，释放锁，然后重新开辟五个线程
            self.sema.acquire()
            spider = SpiderConsumer(url, i, self.sema)
            # 每执行一次start，sema中的value值减小1,
            spider.start()


if __name__ == '__main__':
    # 单次允许的最大开辟的线程
    sema = threading.Semaphore(value=4)
    url_producer = UrlProducer(sema)
    url_producer.start()
