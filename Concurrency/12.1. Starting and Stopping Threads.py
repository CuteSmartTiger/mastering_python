import time
from threading import Thread
# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(2)

# Create and launch a thread
# from threading import Thread
# t = Thread(target=countdown, args=(10,))
# t.start()

# if t.is_alive():
#     print('Still running')
# else:
#     print('Completed')

# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程
# 后台线程无法等待，这些线程会在主线程终止时自动销毁
# t = Thread(target=countdown, args=(10,), daemon=True)
# t.start()

# 2.结束一个线程，或给它发送信号，或调整它的调度，或执行其他高级操作
# 这些特性需要自己添加

# 2.1终止线程
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()   # Signal termination
t.join()       # Wait for actual termination (if needed)


# I/O的阻塞操作
# 2.2 超时循环；
class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)        # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
            ...
        # Terminated
        return