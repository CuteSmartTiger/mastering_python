import threading
import time

# 条件变量,用于复杂的线程间同步
# 本实例主要说明lock锁是无法实现线程同步的
# 因为在一个时间片之内，线程可以多次获取释放锁


class God(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        super().__init__(name='God')

    def run(self):
        self.lock.acquire()
        print(self.name, '问:你是谁？')
        self.lock.release()

        self.lock.acquire()
        print(self.name, '问:你来自哪里？')
        self.lock.release()

# 使用time.sleep()挂起后，CPU进行切换

class Huaman(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        super().__init__(name='Human')

    def run(self):
        self.lock.acquire()
        print(self.name, '答:我是你的白马王子')
        self.lock.release()

        self.lock.acquire()
        print(self.name, '答:来自你的心里')
        self.lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    god = God(lock)
    human = Huaman(lock)
    god.start()
    human.start()
