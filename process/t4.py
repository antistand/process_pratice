import os
import time
from multiprocessing import Process

# names = []  # 全局变量
#
#
# def add_names():
#     global names  # 子进程与主进程是是并发执行的，不能共享全局变量(主进程变量)，只是复制一份
#     names.clear()  # 只会影响子进程的变量，不会影响主进程的变量
#     names.append('Disen at ' + str(os.getpid()))
#
#     time.sleep(2)
#     print('子进程', os.getpid(), names)
#
#
# if __name__ == '__main__':
#     names.append('Jack')
#     names.append('Lucy')
#
#     p = Process(target=add_names)
#     p.start()
#
#     names.append('Cic')
#     print('主进程', os.getpid(), names)

names = ['Disen', 'Lucy']


def add_name(name):
    # global names  # 从主进程中复制一份到当前子进程中，对于进程来说全局变量global可以更改，在线程中global会重新被copy一份新的
    names.clear()
    names.append(name)
    names.append('ABC')
    print('{}子进程修改names:{}'.format(os.getpid(), names))

    time.sleep(2)


if __name__ == '__main__':

    p = Process(target=add_name, kwargs={'name': '康贵喜'})
    p.start()
    p.join()

    names.append('Judy')
    names.append('Cic')

    print('{}主进程修改names:{}'.format(os.getpid(), names))



