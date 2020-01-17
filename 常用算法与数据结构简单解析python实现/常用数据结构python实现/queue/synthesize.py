#! -*- coding=utf-8 -*-
from collections import deque

# 容器里没有值的异常
class NoValueInContainerError(Exception):
    def __init__(self):
        self.message = 'NoValueInContainer！'


# 定义简单的栈结构LIFO
class Stack():
    def __init__(self):
        self.deque = deque()
    
    def push(self, val):
        return self.deque.append(val)
    
    def pop(self):
        return self.deque.pop()
    
    def is_empty(self):
        return len(self.deque) == 0

# 定义简单的队列结构FIFO
class Queue():
    def __init__(self):
        self.items = deque()
    
    def append(self, val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0

'''
例1、
如何用两个栈实现队列
思路：
a栈后进先出，b栈后进先出
实现先进先出
'''
class MyQueue():
    pass

       

'''
例2、
如何实现最小值栈，minStack
实现一个功能，每次获取的它的最小值
'''

'''
例3、
例1的变形，两个队列实现栈
'''