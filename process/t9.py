import time
from multiprocessing import Queue, Process
from os import getpid


def boss(q):
    for i in range(20):
        msg = '领导: {}   派发任务: {}    各位注意接收'.format(getpid(), i)
        time.sleep(2)
        q.put(msg)
        print(time.strftime('%H:%M:%S', time.localtime()), msg)


def worker(q):
    while True:
        time.sleep(2)
        q.get()
        msg = '已收到'
        print(time.strftime('%H:%M:%S', time.localtime()), '呵呵', getpid(), msg)


if __name__ == '__main__':
    q = Queue(maxsize=2)  # 最大消息数量

    workers = []
    for i in range(5):
        work = Process(target=worker, args=(q,))
        work.start()

        workers.append(work)  # 将工人管理起来

    boss(q)  # 老板开始派活

    for worker in workers:
        worker.join()
        worker.terminate()  # 解散工人

    q.close()

    print('---完成工作---')

