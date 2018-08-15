# 12.5. Locking with Deadlock Avoidance

# 问题：在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的
# 方法：解决死锁问题的一种方案是为程序中的每一个锁分配一个唯一的id，然后
# 只允许按照升序规则来使用多个锁，这个规则使用上下文管理器 是非常容易实现的


# 重点：为了避免死锁，所有的加锁操作必须使用 acquire() 函数

# 首先编写上下文管理器
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
# from _thread import _local as local

_local = threading.local()

@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

# 然后按照正常途径创建一个锁对象，但不论是单个锁还
# 是多个锁中都使用 acquire() 函数来申请锁
import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

# 以上方法永远不会出现死锁，但是如果嵌套使用acquire()函数，
# 则可能会发生死锁，示例如下：
import threading
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    # 使用了嵌套
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')

def thread_2():
    # 使用了嵌套
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()