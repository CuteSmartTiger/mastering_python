import multiprocessing
import time


def spider(times):
    time.sleep(times)
    print('子进程成功！！')
    return times


if __name__ == '__main__':
    process = multiprocessing.Process(target=spider, args=(3,))
    print(process)
    process.start()
    print(process.pid)
    process.join(timeout=4)
    print('主进程结束')

    print('=======================')
    # 进程池
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(spider,args=(3,))
    result1 = pool.apply_async(spider,args=(1,))
    # 等待所有子进程完成
    # 此处为什么要用close()
    pool.close()
    # 阻塞
    pool.join()
    print(result.get())
    print(result1.get())

    print('=====================================')
    # imap执行多个子进程
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap(spider,[1,4,2,3]):
        print('{0} sleep ended'.format(result))

    print('====================')
    # imap_unordered
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap_unordered(spider, [1, 4, 2, 3]):
        print('{0} sleep ended'.format(result))