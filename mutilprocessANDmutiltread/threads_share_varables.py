import threading
import time
from random import randint

url_list = []


def get_url_list():
    global url_list
    print('get_url_list:start')
    while True:
        for i in range(10):
            url_list.append('www.studyai.com/' + str(randint(1, 2000)) + '/')
        time.sleep(2)
        print('生产者有生产了10个URL')


def get_html_detail(id):
    global url_list
    print('get_html_detail:start')
    # 模拟爬取信息，每次爬取一个网页需要时间为1秒
    while True:
        print('剩余URL个数：', len(url_list))
        if len(url_list) > 0:
            url = url_list.pop()
            print(str(id), '正在获取详情:', url)
            time.sleep(1)
        else:
            print('get_html_detail:end')
            break


if __name__ == "__main__":
    time_start = time.time()
    # 如果此处daemon=True，则生产者与消费者不会循环,
    # 此时主线程结束后会关闭子线程
    list_thread = threading.Thread(target=get_url_list, daemon=False)
    list_thread.start()
    # 此处不可以使用join，否则会陷入while true的不断执行中
    # list_thread.join()
    detail_threads = []
    for i in range(5):
        detail_thread = threading.Thread(target=get_html_detail, args=(i,),
                                         daemon=False)
        detail_threads.append(detail_thread)
        detail_thread.start()
        # detail_thread.join()
    consumed_time = time.time() - time_start
    print(consumed_time)
