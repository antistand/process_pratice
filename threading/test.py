def producer(l): # 生产者
    i = 0
    while True:
        if i < 10:
            l.append(i)
            print('producer', i)
            yield i
            i = i + 1
            time.sleep(1)
        else:
            return

# 消费者

# 消费者
def consumer(l):
    p = producer(l)
    while True:
        try:
            next(p)
            while len(l) > 0:
                print('consumer', l.pop())
        except:
            pass

# 测试

if __name__ == "__main__":
    l = [] # 数据
    consumer(l)
