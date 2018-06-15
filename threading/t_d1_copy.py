import threading
import time
from random import randint

# data = threading.local()
data = 100


def add_money():
    data.v = 100  # 当全局变量需要参与运算时，必须将其global声明
    for i in range(10):

        m = randint(50, 100)
        time.sleep(2)
        print('子线程{}正在修改money:{}+{}'.format(threading.current_thread().name, data.v, m))
        data.v += m
    time.sleep(5)
    print('线程{}余额{}'.format(threading.current_thread().name, data.v))


if __name__ == '__main__':
    # 生成5个线程
    ts = [threading.Thread(target=add_money, name='worker' + str(i)) for i in range(5)]
    for t in ts:
        t.start()
    # raise Exception('went wrong')  主线程抛出异常，子线程不受影响，前提是线程使用本地变量

    print('--最终结果--')

