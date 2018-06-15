import os
import time
from math import trunc
from multiprocessing import Value, Process
from random import uniform, randint


def modify_money(money, m):
    time.sleep(2)

    print(os.getpid(), '子进程修改money之前: ', money.value)

    money.value += m
    print(os.getpid(), '---子进程增加---',  m, '余额', money.value)


if __name__ == '__main__':
    # 创建float类型的对象
    money = Value('f', 100)  # 进程之间共享变量，必须通过c语言共享变量来完成
    ps = [Process(target=modify_money, args=(money, trunc(uniform(100, 500)))) for i in range(5)]

    for p in ps:
        p.start()

    for p in ps:
        p.join()

    print('---main 执行完成---', money.value)

