# 本模块需要了解的知识点：
# queue中使用的deque，get,put，join，empty，qsize等方法
# 使用queue的原因，为什么会安全
# 用queue来实现线程之间的安全通信，主要指再字节码或时间片内时安全的
import threading
import time
from random import randint

# 此处的Queue的只能用于线程之间的通信
from queue import Queue


def get_url_list(url_queue):
    print('get_url_list:start')
    while True:
        for i in range(10):
            url_queue.put('www.studyai.com/' + str(randint(1, 2000)) + '/')
        time.sleep(2)
        print('生产者有生产了10个URL')


def get_html_detail(id, url_queue):
    print(str(id), 'get_html_detail:start')
    # 模拟爬取信息，每次爬取一个网页需要时间为1秒
    while True:
        print('剩余URL个数：', url_queue.qsize())
        if not url_queue.empty():
            url = url_queue.get()
            print(str(id), '正在获取详情:', url)
            time.sleep(1)
        else:
            # print('get_html_detail:end')
            # print('URL个数为空')
            print('URL队列为空')
            # break


if __name__ == "__main__":
    time_start = time.time()
    url_queue = Queue(maxsize=50)
    # 如果此处daemon=True，则生产者与消费者不会循环,
    # 此时主线程结束后会关闭子线程
    list_thread = threading.Thread(target=get_url_list, args=(url_queue,), daemon=False)
    list_thread.start()
    # 此处不可以使用join，否则会陷入while true的不断执行中
    # list_thread.join()
    detail_threads = []
    for i in range(5):
        detail_thread = threading.Thread(target=get_html_detail, args=(i, url_queue),
                                         daemon=False)
        detail_threads.append(detail_thread)
        detail_thread.start()
        # detail_thread.join()
    # 主线程会等待子线程结束后再继续执行
    url_queue.join()
    consumed_time = time.time() - time_start
    print(consumed_time)
