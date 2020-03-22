#! -*- encoding=utf-8 -*-
import threading, time

# 定义错误
class ThreadSafeQueueException(Exception):
    pass

# 线程安全的队列
class ThreadSafeQueue(object):
    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size
        self.lock = threading.Lock()                # 互斥量
        self.condition = threading.Condition()      # 条件变量

    # 当前队列元素的数量
    def size(self):
        self.lock.acquire()         # 我们获取数量的时候可能会被修改所以先加锁
        size = len(self.queue)
        self.lock.release()         # 获取完数量就把锁释放掉
        return size
    
    # 往队列里面放入元素
    def put(self, item):
        if self.max_size != 0 and self.size() > self.max_size:
            return ThreadSafeQueueException
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()
        '''
        假设现在队列为0，其他想要获取的时候就会阻塞，那么这时候加入元素后这个条件变量就会去通知阻塞的线程来取
        '''


    # 往队列里面批量放入元素
    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)
    
    # 从队列取出元素, pop默认从队列头部取出元素
    def pop(self, block=False, timeout=0):   # 第一个参数是否默认等待，第二个参数等待多久
        if self.size() == 0:
            # 如果需要阻塞等待：
            if block:
                self.condition.acquire()
                self.condition.wait(timeout=timeout)
                self.condition.release()
            else:
                return None
        '''
        # 如果等待传入的时间还是没有拿到值那么我们还是返回None
        if self.size() == 0:
            return None
        # 如果不为空，取出元素
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        return item
        以上是有问题的：
        这个逻辑：
        if self.size() == 0:
            return None
        和这个逻辑：
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        是分开的，而第一个逻辑没有被锁保护，所以不是原子性的，
        那么如果第一段逻辑判断完size发生变化，那么代码就会有问题。
        '''
        self.lock.acquire()
        item = None
        if len(self.queue) > 0:
            item = self.queue.pop()
        self.lock.release()
        return item
    
    # 拿出指定index的元素
    def get(self,index):
        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
        return item

# 测试
if __name__ == "__main__":
    queue = ThreadSafeQueue(max_size = 100)
    def producer():
        while True:
            queue.put(1)
            time.sleep(1)
            print("produce all : %d", queue.size())      #生产时间
    def consumer():
        consumer_product = []
        while True:
            item = queue.pop(block=True, timeout=2)
            print("get item from the queue: %d" % item)
            consumer_product.append(item)
            print("consumer have : %d", len(consumer_product))
            time.sleep(2)
    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()