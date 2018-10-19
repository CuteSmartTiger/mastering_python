import threading
import time
from random import randint

url_list = []


def get_url_list():
    print('get_url_list:start')
    for i in range(10):
        url_list.append('www.studyai.com/' + str(randint(1, 2000)) + '/')
    time.sleep(2)
    print('get_url_list:end')


def get_html_detail(url):
    print('get_html_detail:start')
    # 模拟爬取信息，每次爬取一个网页需要时间为1秒
    for url in url_list:
        print('正在获取详情:', url)
        time.sleep(1)
    print('get_html_detail:end')


if __name__ == "__main__":
    list_thread = threading.Thread(target=get_url_list, daemon=False)
    # list_thread = threading.Thread(target=get_url_list, daemon=True)
    # detail_thread = threading.Thread(target=get_html_detail, args=('www.studyai.com',), daemon=False)
    # 子进程中daemon设置为True，则意味这个子进程再执行的过程中一旦发现主进程已结束以及其他进程也结束，则会立即结束自己的进程，目前暂时这么理解
    detail_thread = threading.Thread(target=get_html_detail, args=('www.studyai.com',), daemon=True)
    time_start = time.time()
    list_thread.start()
    detail_thread.start()
    # list_thread.join()
    # detail_thread.join()
    consumed_time = time.time() - time_start
    print(consumed_time)

# 当daemon为False，没有join时，主线程main与子线程一起执行，主线程结束时子线程可以继续执行
# 当daemon为True，没有join时，主线程main执行完后，若其他设置为false的子线程已经结束，而为True的子线程还没执行完毕，依然关闭主线程及子线程
# 当daemon为True，join存在时，join会通知主线请等待，若子线程还没执行完毕，则主线程等待join通知的子线程结束后再执行
