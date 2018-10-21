# 进程之间的通信，这里不可以使用queue中的Queue，必须使用mutilprocessing中的Queue，进程之间无法使用全局变量进行通信
import time
from multiprocessing import Queue,Process


def producer(queue):
    id_num =1
    while True:
        queue.put('{0}号面包'.format(id_num))
        print('生产了一个面包，编号为{0}'.format(id_num))
        id_num+=1
        time.sleep(2)

def consumer(queue):
    while True:
        time.sleep(2)
        data = queue.get()
        print('消费了{0}'.format(data))


if __name__ == '__main__':
    queue = Queue(6)
    myproducer = Process(target=producer,args=(queue,))
    myconsumer = Process(target=consumer,args=(queue,))
    myproducer.start()
    myconsumer.start()
    myconsumer.join()
    myproducer.join()