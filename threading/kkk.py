
import time
from multiprocessing import Manager, Process


def producer(ids, lock):
    while True:
        print(lock)
        with lock:
            ids.value = ids.value + 1
        yield 'product' + str(ids.value)


def consumer(name, ids, lock, times):
    while True:
        print(lock)
        product = next(producer(ids, lock))
        with lock:
            print(name, 'consume:', product)
        time.sleep(times)


if __name__ == '__main__':
    manager = Manager()
    lock = manager.Lock()
    ids = manager.Value('f', 1)

    p1 = Process(target=consumer, args=('A', ids, lock, 1))
    p2 = Process(target=consumer, args=('B', ids, lock, 1))
    p3 = Process(target=consumer, args=('C', ids, lock, 1))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()