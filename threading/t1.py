import time
from threading import Thread


class MineTed(Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def gene_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def run(self):
        for i in range(200):
            print(self.gene_time(), '：  {}  正在执行： {}'.format(i, self.name))


# def worker(word):
    # for i in range(50):
    #     time.sleep(1)
        # print('今天是： {}， 我是搬了{}个{}的小蜜蜂'.format(MineTed('disen').gene_time(), i, word))


# ts = [Thread(target=worker, args=('砖',)) for i in range(3)]

ts = [MineTed(i) for i in range(3)]


for t in ts:
    t.start()

for t in ts:
    t.join()

