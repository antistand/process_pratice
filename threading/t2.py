# 声明全局变量
import time
from threading import Thread, Lock

money = 1000

# 存钱


# 存钱
def add(n, lock):
    for i in range(6):
        print(n, '开始第{}次存款'.format(i))
        lock.acquire()
        try:
            global money
            sm = 1000
            money += sm
            print(n, '线程存了', sm, '剩余：', money)
            time.sleep(1)
        except:
            pass
        finally:
            lock.release()

# 取钱


# 取钱
def sub(n, lock):
    for i in range(3):
        print(n, '开始第{}次取款'.format(i))
        lock.acquire()
        try:
            global money
            print(n, '-取钱之前-', money)
            sm = 1000
            money -= sm
            print(n, '线程取了{} 之后 剩余:'.format(sm), money)
            time.sleep(2)
        except:
            pass
        finally:
            lock.release()


# 程序入口

if __name__ == '__main__':

    lock = Lock()

    t1 = Thread(target=add, args=(1, lock))
    t2 = Thread(target=sub, args=(2, lock))
    t3 = Thread(target=sub, args=(3, lock))

    t1.start()
    t2.start()
    t3.start()
