#! -*- coding=utf-8 -*-
'''
队列，先进先出，FIFO
单端队列
双端队列
主要方法：pop和append
利用list和内置的collections.deque双端队列实现
'''
# 用deque实现 队列
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    
    def append(self, val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0

def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())

test_queue()