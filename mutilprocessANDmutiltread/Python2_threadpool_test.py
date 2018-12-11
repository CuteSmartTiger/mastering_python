#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 16:25
# @Author  : liuhu
# @File    : Python2_threadpool_test.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import threading
from threadpool import *
if __name__ == '__main__':
    import random
    import time

    # 线程必须做的工作（在我们的例子中相当微不足道）
    def do_something(data):
        time.sleep(random.randint(1,5))
        result = round(random.random() * data, 5)
        # 仅仅抛出异常，不做任何处理
        if result > 5:
            raise RuntimeError("Something extraordinary happened!")
        return result

    # 打印结果
    def print_result(request, result):
        print("**** Result from request #%s: %r" % (request.requestID, result))

    # 线程内有异常时，处理异常，这里做的比默认异常处理还要简单
    def handle_exception(request, exc_info):
        if not isinstance(exc_info, tuple):
            # 肯定有错误发生
            print(request)
            print(exc_info)
            raise SystemExit
        print("**** Exception occured in request #%s: %s" % \
          (request.requestID, exc_info))


    # 产生一个具有20个元素的列表，元素大小范围为（1,10），作为每项工作的参数
    data = [random.randint(1,10) for i in range(20)]
    # 为data中的每一项构建一个工作请求对象
    requests = makeRequests(do_something, data, print_result, handle_exception)
    # 如果想要使用默认异常处理，则注释掉这条语句，使用下面这条语句
    #requests = makeRequests(do_something, data, print_result)

    # or the other form of args_lists accepted by makeRequests: ((,), {})
    # data = [((random.randint(1,10),), {}) for i in range(20)]
    # requests.extend(
    #     makeRequests(do_something, data, print_result, handle_exception)
    # )
    #requests += makeRequests(do_something, data, print_result, handle_exception)

    # 创建拥有 3个工作线程的线程池
    print("Creating thread pool with 3 worker threads.")
    main = ThreadPool(3)

    # 把工作请求加入到队列中
    for req in requests:
        main.putRequest(req)
        print("Work request #%s added." % req.requestID)
    # 或使用更短语句:
    # [main.putRequest(req) for req in requests]

    # ...and wait for the results to arrive in the result queue
    # by using ThreadPool.wait(). This would block until results for
    # all work requests have arrived:
    # main.wait()

    # instead we can poll for results while doing something else:
    i = 0
    while True:
        try:
            time.sleep(0.5)
            main.poll()
            print("Main thread working...")
            print("(active worker threads: %i)" % (threading.activeCount()-1, ))
            if i == 10:
                print("**** Adding 3 more worker threads...")
                main.createWorkers(3)
            if i == 20:
                print("**** Dismissing 2 worker threads...")
                main.dismissWorkers(2)
            i += 1
        except KeyboardInterrupt:
            print("**** Interrupted!")
            break
        except NoResultsPending:
            print("**** No pending results.")
            break
    if main.dismissedWorkers:
        print("Joining all dismissed worker threads...")
        main.joinAllDismissedWorkers()
