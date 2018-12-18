import threading
import time
from threading import Condition


# 条件变量用于复杂的线程间通信
# 本节证明可以使用Condition实现线程间的同步
# Condition中需要了解的知识点：
# 1. 实现了enter exit魔法方法，可以使用with
# 2. acquire，在enter方法中定义
# 3. release，在exit方法中定义
# 4. wait，等待某个条件变量的通知
# 5. notify，通知调用了wait方法的线
# 程启动，显然wait与notify之间通信了
# 6.源码中双端队列的使用


class God(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name='God')

    def run(self):
        # 先获取condition
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
    # 启动顺序很重要
    # 如果先启动god，则god瞬间先执行到notify这步，
    # 而human后启动，则wait无法收到god的通知
    # 调用with cond 之后才能调用wait或者notify方法
    # god.start()
    # human.start()
    #condition有两把锁，一把底层锁会在线程调用wait
    # 方法的时候释放，上面的锁会在调用wait的时候分
    # 配一把并放入到cond的等待队列中，等待notify方
    # 法的唤醒
    human.start()
    god.start()
