import threading
import time


class GetUrlList(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name, ':start')
        time.sleep(3)
        print(self.name, ':end')


class GetHtmlDetail(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(self.name, ':start')
        time.sleep(4)
        print(self.name, ':end')


# 使用场景：线程池中使用自带的方法，若run方法比较复杂，则考虑下面这种自定义的方法
if __name__ == "__main__":
    list_thread = GetUrlList(name='get_url_list')
    detail_thread = GetHtmlDetail(name='get_html_detail')
    list_thread.setDaemon(True)
    detail_thread.setDaemon(True)
    time_start = time.time()
    list_thread.start()
    detail_thread.start()
    list_thread.join()
    detail_thread.join()
    consumed_time = time.time() - time_start
    print(consumed_time)
