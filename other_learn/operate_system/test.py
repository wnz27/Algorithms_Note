#! -*- encoding=utf-8 -*-
import time

from other_learn.operate_system.task import Task
from other_learn.operate_system.pool import ThreadPool

# 定义一些任务
class SimpleTask(Task):
    def __init__(self, callable):
        super.__init__(callable)

def process(test):
    print("This is %d's Simple callable function!", test)
    time.sleep(1)

def test():
    # 1、初始化一个线程池
    test_pool = ThreadPool()
    test_pool.start()
    # 2、生成一系列任务
    for i in range(10):
        simple_task = SimpleTask(process(str(i)))
        # 3、往线程池提交任务执行
        test_pool.put(simple_task)
    pass

if __name__ == "__main__":
    test()