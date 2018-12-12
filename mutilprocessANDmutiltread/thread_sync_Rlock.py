from threading import RLock

# RLock:可重入锁，在同一个线程中可以连续多次调用acquire获得锁，
# 但是必须连续调用同样次数的release来释放锁

# RLock主要是解决lock获取一个后必须释放一个锁的缺点，可以在函数中调用函数，嵌套使用锁
total = 0

# 获取锁这个对象
lock = RLock()


def mutil(lock):
    global total
    lock.acquire()
    total *= 1
    lock.release()
    return total


def add(ran):
    """
    :param ran: int
    :return: int
    """
    global total, lock
    for i in range(ran):
        # 通过dis我们知道运行结果不一样病发生争抢在于代码
        # 片执行中有对变量的暂时存储，所以可以对变量加锁
        lock.acquire()
        total += 1
        # 函数中调用函数，主要是解决lock获取一个后必须释放一个锁的缺点
        mutil(lock)
        lock.release()
    print(total)
    return total


def sub(ran):
    """
    :param ran: int
    :return: int
    """
    global total, lock
    for i in range(ran):
        lock.acquire()
        total -= 1
        lock.release()
    print(total)
    return total


# 在main一个主线程下开辟了两个子线程
if __name__ == "__main__":
    from threading import Thread

    # 此处还需理解daemon用法
    # add_thread = Thread(target=add, args=(1000000,), daemon=True)
    add_thread = Thread(target=add, args=(1000000,))
    # sub_thread = Thread(target=sub, args=(1000000,), daemon=True)
    sub_thread = Thread(target=sub, args=(1000000,))
    add_thread.start()
    sub_thread.start()
    # join表示通知主线程，对应的子线程结束后方可执行主线程
    # add_thread.join()
    # sub_thread.join()
    print(total)


