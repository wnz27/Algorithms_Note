'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-07 07:54:27
@LastEditTime: 2020-03-07 08:07:33
@FilePath: /Algorithms_Note/数据结构与算法基础学习/stack_interface.py
@description: type some description
'''
from abc import ABCMeta, abstractmethod
'''
栈接口
'''
class Stack(metaclass=ABCMeta):
    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass