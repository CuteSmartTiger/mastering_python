# 13.13. Making a Stopwatch Timer
# 目的：记录程序执行多个任务所花费的时间
import time


# print(time.perf_counter())
# print(time.time())


class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


def countdown(n):
    while n > 0:
        n -= 1


# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)

# Use 2: As a context manager
# 思考：此处执行时间是其他的两倍多，为什么
# 当把print(t.elapsed)缩进时则执行时间与其他相同
with t:
    countdown(1000000)
print(t.elapsed)

with Timer() as t2:
    countdown(1000000)
print(t2.elapsed)

t = Timer(time.process_time)
with t:
    countdown(1000000)
print(t.elapsed)
