import threading
import time
from queue import Queue  # 线程间通信，需要引入的是queue
from threading import Condition, Lock


class ConcurrentQueue:
    def __init__(self, max_size=10):
        self.max_size = max_size  # 满仓量
        self.lock = Lock()  # 互斥对象
        self.cond = Condition(self.lock)
        self.q = Queue()  # 数据对象（仓库）

# 获取数据（消费）

    def get(self):  # 获取队列的数据
        # 获取互斥锁和条件变量（默认包含互斥量）
        if self.cond.acquire():
            while self.q.empty():
                print('仓库已空, 请等待...')
                self.cond.wait()  # 条件变量等待

            obj = self.q.get()  # 获取要消息数据
            self.cond.notify()  # 通知等待的生产者线程，开始消费了。。。
            self.cond.release()  # 释放锁
        return obj

# 存入数据（生产）

    def put(self, obj):
        if self.cond.acquire():
            # 仓库为满时，无法再生产
            while self.q.qsize() >= self.max_size:
                print('仓库已满，请等待生产...')
                self.cond.wait()  # 条件变量等待

            # 仓库未满，可以再生产
            self.q.put(obj)

            self.cond.notify()  # 通知等待的消费者线程，已经生产了
            self.cond.release()  # 释放锁

# 生产者函数


def producer(cq: ConcurrentQueue):
    n = 1
    while True:
        cq.put('馒头 %d' % n)
        print(threading.current_thread().name, '已生产馒头 %d' % n)
        time.sleep(0.2)
        n = n + 1


def consumer(cq: ConcurrentQueue):
    while True:
        bread = cq.get()
        print(threading.current_thread().name, '已消费', bread)
        time.sleep(0.5)


# 程序入口测试

if __name__ == '__main__':
    cq = ConcurrentQueue(20)
    # 创建消费者线程
    cts = [threading.Thread(target=consumer, args=(cq,), name='老狗') for i in range(3)]
    # 创建生产者线程
    pts = [threading.Thread(target=producer, args=(cq,), name='老鬼') for i in range(2)]

    for ct in cts:
        ct.start()

    for pt in pts:
        pt.start()





