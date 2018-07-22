import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
s = Spam()
print(s.instance_method(1000000))
# <__main__.Spam object at 0x1006a6050> 1000000
# 0.11817407608032227
print(Spam.class_method(1000000))
# <class '__main__.Spam'> 1000000
# 0.11334395408630371
print(Spam.static_method(1000000))
# 1000000
# 0.11740279197692871

