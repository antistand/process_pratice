import os
import time
from multiprocessing import Process, Manager


def produce():
    i = 0
    while True:
        i = i + 1
        print('{}: 已生产: {}，等待消费'.format(os.getpid(), i))
        yield i
        time.sleep(0.5)


def consumer(p, name, ids):
    for i in range(20):
        msg = next(p)
        ids.value = ids.value + 1
        print('id: {}, {}消费了{}, ids: {}'.format(os.getpid(), name, msg, ids.value))  # 获取生产信息
        print('主进程', os.getppid())


if __name__ == '__main__':

    p1 = produce()
    manager = Manager()
    ids = manager.Value('k', 8)

    c1 = Process(target=consumer, args=(p1, 'A', ids))
    c2 = Process(target=consumer, args=(p1, 'B', ids))
    c3 = Process(target=consumer, args=(p1, 'C', ids))

    c1.start()
    c2.start()
    c3.start()

    c1.join()
    c2.join()
    c3.join()

    print('--over--', os.getpid())
