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
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.count = 0
    
    def push(self, val):
        if not self.stack1.push(val):
            self.count += 1
            return True
        else:
            return False

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        res = self.pop()
        self.push(res)
        return res

    def pop(self):
        if self.count == 0:
            raise NoValueInContainerError()
        else:
            count = self.count  # 记录原始数据数量
            while count != 0:  # 把栈1的数据倒入栈2
                self.stack2.push(self.stack1.pop())
                self.count -= 1
            res = self.stack2.pop() # 记录要返回的数据
            while self.count != count - 1:  # 此时已经pop出一个数据了, 把栈2的数据倒回栈1
                self.stack1.push(self.stack2.pop())
                self.count += 1
            return res

    def empty(self):
        return self.stack1.is_empty() & self.stack2.is_empty()


'''
例2、
如何实现最小值栈，minStack
实现一个功能，每次获取的它的最小值
'''

'''
例3、
例1的变形，两个队列实现栈
'''