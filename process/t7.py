import os
import time
from multiprocessing import Array, Process

names = Array('c', range(20))  # range(20) 只是指定一个字符数组的长度大小


def add_name(name):
    print(os.getpid(), '子进程修改前names:', names.value)
    names.value = name.encode()  # 在子进程修改主进程变量
    print(os.getpid(), '子进程修改后names:', names.value)
    time.sleep(2)


if __name__ == '__main__':

    names.value = b'Disen'  # names是Array类对象，存储字节类型的数据

    p = Process(target=add_name, kwargs={'name': 'ABC'})

    p.start()
    p.join()

    print('主进程结束--names: ', names.value)
