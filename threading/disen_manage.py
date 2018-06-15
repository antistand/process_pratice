# from multiprocessing import Value, Process, Lock
# from multiprocessing.managers import BaseManager
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
    pass


MyManager.register('User', User)


# def Manager():
#     m = MyManager()
#     m.start()
#     return m


def f(user, lock):
    with lock:
        user.increase()
        print('子进程', user)


if __name__ == '__main__':
    manage = MyManager()
    manage.start()
    user = manage.User('disen', 0)
    lock = Lock()
    p1 = [Process(target=f, args=(user, lock)) for i in range(10)]

    for p in p1:
        p.start()

    for p in p1:
        p.join()
    print('主进程', user)
