import os
import time
from multiprocessing import Pipe, Process


def sender(conn):
    while True:
        msg = '您好，我是Disen'
        print('----------发送消息<{}>: {}-----------'.format(os.getpid(), msg))
        conn.send(msg)
        time.sleep(1)
        print('回复: ', conn.recv())


def receiver(conn):
    while True:
        print(conn.recv())

        msg = '已收到'
        time.sleep(3)
        conn.send(msg)


if __name__ == '__main__':
    pipe = Pipe()  # 返回一个元组(conn1, conn2)
    p1 = Process(name='发送者', target=sender, args=(pipe[0],))
    p2 = Process(name='接收者', target=receiver, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()  # 在主线程中，等待子线程完成
    p2.join()
    print('---over---')
