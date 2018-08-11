# 13.14. Putting Limits on Memory and CPU Usage

# (只用于 Unix , 可选) resource 模块用于查询或修改当前系统资源限制设
# 可以在这个网站看到Unix系统的特殊模块：
# https://docs.python.org/3/library/unix.html
import signal
import resource
import os


def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)

def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)

if __name__ == '__main__':
    set_max_runtime(5)
    while True:
        pass
