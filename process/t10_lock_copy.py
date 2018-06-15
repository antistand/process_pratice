import os
import time
from multiprocessing import Process, Value, Lock
from multiprocessing.managers import BaseManager


class User:
    def __init__(self, name, salary):
        self.name = name
        self.money = Value('f', salary)

    def increase(self):
        self.money.value = self.money.value + 1000
        time.sleep(1)

    def __repr__(self):
        return '{} money is {}'.format(self.name, self.money.value)


class MyManager(BaseManager):
    pass  # 继承了BaseManager则就继承了基本的Manager功能，不需要再添加更多了




def Manager():
    m = MyManager()
    m.start()
    return m


def f(user, lock):
    with lock:
        user.increase()
        print(os.getpid(), '子进程', user)


if __name__ == '__main__':
    MyManager.register('User', User)

    manage = Manager()
    user = manage.User('disen', 1000)
    lock = Lock()

    # procs = [Process(target=f, args=(user, lock)) for i in range(5)]
    p1 = Process(target=f, args=(user, lock))

    p1.start()
    p1.join()
    # for proc in procs:
    #     proc.start()
    #
    # for proc in procs:
    #     proc.join()

    print('主进程', os.getpid(), user)

