#! -*- encoding=utf-8 -*-
import threading
import psutil
from other_learn.operate_system.task import Task
from other_learn.operate_system.queue import ThreadSafeQueue

# 实现任务处理线程
class ProcessThread(threading.Thread):
    def __init__(self, task_queue, *args, **kwargs):
        # 因为继承的所以先调用父类的构造函数
        threading.Thread.__init__(self, *args, **kwargs)
        # 线程停止的标记
        self.dismiss_flag = threading.Event()
        # 任务队列（处理线程不断从队列取出任务来处理）
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑（是通过函数调用引进来的）
            result = task.callable(task.func, *task.args, **task.kwargs)
    
    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()

# 实现线程池
class ThreadPool:
    def __init__(self, size=0):
        if not size:
            # 约定线程池的大小为cpu核数的两倍 （经验上的最佳实践）
            size = psutil.cpu_count() * 2
        # 线程池
        self.pool = ThreadSafeQueue(size)  
        # 任务队列
        self.task_queue = ThreadSafeQueue()
        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    # 启动线程池方法
    def start(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.run()   # 有疑问
    
    # 停止线程池方法!!!!!!!
    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop()
        while self.pool.size():
            thread = self.pool.pop()    # 把线程推出去
            thread.join()               # 等待推出的线程停止
        # 把线程池里所有线程都停止且清空了才是真正停止线程池
    
    # 往线程池提交任务的方法
    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException()
        self.task_queue.put(item)
    
    # 批量提交的方法
    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)
    
    def size(self):
        return self.pool.size()

class TaskTypeErrorException(Exception):
    pass
