import os
import time
from multiprocessing import Process


def study(name, course_name):
    while True:
        print('子进程：{}, 所属父进程：{}, {}正在学习，学习{}'.format(os.getpid(), os.getppid(), name, course_name))
        time.sleep(2)


def praise(name):
    while True:
        print('子进程：{}, {}学习真好'.format(os.getpid(), name))  # os.getpid()获取当前函数所在的进程id
        time.sleep(2)


if __name__ == '__main__':
    # 让学习在子进程中使用
    # 查看括号参数，ctrl+p  # cpu创建独立的内存和线程来运行target任务
    # 关键参数传值，通过字典的键值对进行传值
    study_process = Process(target=study, kwargs={'name': '康贵喜', 'course_name': '高能物理'})
    study_process.start()

    praise_process = Process(target=praise, args=('康贵喜',))
    praise_process.start()

    # 主进程抛出异常
    raise Exception('我是一只小青蛙')

    study_process.join(timeout=10)  # 必须等到所有进程加入之后才可以join，如果join写到前面，会造成阻塞后果
    praise_process.join(timeout=10)  # timeout超时时间，如果子进程在10秒内没有执行结束，主线程就立即向后执行，不会再等待
    print('主进程：{}, ---over---'.format(os.getppid()))  # kill -9干掉进程

# eatProcess = Process(target=eat, kwargs={'something': '苹果', 'food': '米饭'})
