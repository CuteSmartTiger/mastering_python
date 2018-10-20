import threading
import time

# 条件变量用于复杂的线程间通信
# 本模块证明使用lock是无法实现线程间的同步的

class God(threading.Thread):
    def __init__(self,lock):
        self.lock = lock
        super().__init__(name='God')

    def run(self):
        self.lock.acquire()
        print(self.name, '问:你是谁？')
        self.lock.release()
        time.sleep(1)
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
        time.sleep(2)
        self.lock.acquire()
        print(self.name, '答:来自你的心里')
        self.lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    god = God(lock)
    human = Huaman(lock)
    god.start()
    human.start()
