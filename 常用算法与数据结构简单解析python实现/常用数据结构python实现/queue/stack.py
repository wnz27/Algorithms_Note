#! -*- coding=utf-8 -*-
'''
栈
后进先出
主要方法：push和pop
利用list和内置的collections.deque双端队列实现
'''
from collections import deque

class Stack():
    def __init__(self):
        self.deque = deque()        # 或者用list
    
    def push(self, val):
        return self.deque.append(val)
    
    def pop(self):
        return self.deque.pop()

def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

test_stack()