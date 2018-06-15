from multiprocessing import Process, Value, Lock
import os
import time
from multiprocessing.managers import BaseManager


class User:
    def __init__(self, name, salary):
        self.name = name
        self.money = Value('f', salary)  # 进程共享变量

    def increase(self):
        self.money.value += 1000
        time.sleep(1)

    def __repr__(self):  # 返回一个string格式的对象
        return '{} money is {}'.format(self.name, self.money.value)


class MyManager(BaseManager):
    # 自定义Manager
    pass


# 向管理器中注册模型类的类型
MyManager.register("User", User)


def Manager():  # 定义创建Manager类对象的函数
    m = MyManager()
    m.start()  # 注意： BaseManager对象必须要启动,  即 start()
    return m


def f(user, lock):
    with lock:
        user.increase()
        print(os.getpid(), '子进程', user)


if __name__ == '__main__':
    manager = Manager()  # 多进程间的数据管理器
    user = manager.User('disen', 100)  # 用manager对象直接对User进行管理

    lock = Lock()
    procs = [Process(target=f, args=(user, lock)) for i in range(5)]
    # 五个进程直接一起搞f函数，就传进去一个user = manager.User('disen', 100)对象和进程锁lock
    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    print('主进程', os.getpid(), user)

