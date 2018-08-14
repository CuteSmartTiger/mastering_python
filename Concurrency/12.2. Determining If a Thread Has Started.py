
# 1.Event
# 原理基础知识：Event 对象包含一个可由线程设置
# 的信号标志，它允许线程等待某些事件的发生。在
# 初始情况下，event 对象中的信号标志被设置为假。
# 如果有线程等待一个 event 对象，而这个 event 对
# 象的标志为假，那么这个线程将会被一直阻塞直至该
# 标志为真。一个线程如果将一个 event 对象的信号标
# 志设置为真，它将唤醒所有等待这个 event 对象的线程

from threading import Thread, Event
import time

# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    # 此处在后续关联event对象
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10,started_evt))
t.start()

# Wait for the thread to start
# 线程一旦启动，则执行print函数
started_evt.wait()
print('countdown is running')

# 2.Condition
# 如果一个线程需要不停地重复使用 event 对象，你最好使用
# Condition 对象来代替。下面的代码使用 Condition 对象实
# 现了一个周期定时器，每当定时器超时的时候，其他线程都可
# 以监测到
import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1
                 self._cv.notify_all()

    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(0.5)
ptimer.start()

# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()


import threading
# 3.Semaphore
# event对象的一个重要特点是当它被设置为真时会唤醒所有等待
# 它的线程。如果你只想唤醒单个线程，最好是使用信号量

# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()

    # Do some work
    print('Working', n)

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

sema.release()
# Working 0
sema.release()
# Working 1