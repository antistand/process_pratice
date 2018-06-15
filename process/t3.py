import os
import time
from multiprocessing.pool import Pool


def study(course):
    for i in range(3):
        print('学习进程： {}，正在学习： {}'.format(os.getpid(), course))
        time.sleep(2)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(processes=5)  # 创建5个子进程，反正一共是五个子进程，无论怎么干掉，都会自动创建至五个子进程

    cs = ['python' + str(i) for i in range(1, 11)]
    for i in range(10):
        pool.apply_async(study, args=(cs[i],))  # args传值，传递cs第[i]个参数

    # 关闭进程池，停止派发任务
    pool.close()

    # 主进程要等待所有的子进程结束任务，
    pool.join()
    print('主进程--over--', os.getpid())
