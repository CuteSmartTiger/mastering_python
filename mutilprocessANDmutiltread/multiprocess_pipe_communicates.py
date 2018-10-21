# 进程之间的通信，这里不可以使用queue中的Queue，必须使用mutilprocessing中的Queue，进程之间无法使用全局变量进行通信
import time
from multiprocessing import Queue, Process, Manager, Pool, Pipe


def producer(pipe):
    id_num = 1
    while True:
        pipe.send('{0}号面包'.format(id_num))
        print('生产了一个面包，编号为{0}'.format(id_num))
        id_num += 1
        time.sleep(1)

def consumer(pipe):
    while True:
        data = pipe.recv()
        print('消费了{0}'.format(data))
        time.sleep(1)


if __name__ == '__main__':
    # pipe只能用于两个进程之间的通信，效率比较高，因为锁比较少
    recv_pipe, send_pipe = Pipe()
    myproducer = Process(target=producer, args=(send_pipe,))
    myconsumer = Process(target=consumer, args=(recv_pipe,))
    myproducer.start()
    myconsumer.start()
    myconsumer.join()
    myproducer.join()
    print('生产消费完毕')
