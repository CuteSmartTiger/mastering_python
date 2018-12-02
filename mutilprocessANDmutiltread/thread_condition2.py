import threading
import time


# 条件变量用于复杂的线程间通信
# 本模块证明使用lock是无法实现线程间的同步的

class God(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name='God')

    def run(self):
        with self.cond:
            print(self.name, '问:你是谁？')
            self.cond.notify()
            self.cond.wait()
            print(self.name, '问:你来自哪里？')
            self.cond.notify()
            self.cond.wait()


class Huaman(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name='Human')

    def run(self):
        with self.cond:
            # 启动线程的监听，一直准备接收信息
            self.cond.wait()
            print(self.name, '答:我是你的白马王子')
            # 通知另一个线程阶段性事情已经完成
            self.cond.notify()
            self.cond.wait()
            print(self.name, '答:来自你的心里')
            self.cond.notify()


if __name__ == '__main__':
    cond = threading.Condition()
    god = God(cond)
    human = Huaman(cond)
    # 如果先启动god，则god瞬间先执行到notify这步，
    # 而human后启动，则wait无法收到god的通知
    # god.start()
    # human.start()
    human.start()
    god.start()
