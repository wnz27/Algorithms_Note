'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-07 07:54:09
@LastEditTime: 2020-03-07 11:12:18
@FilePath: /Algorithms_Note/数据结构与算法基础学习/queue_interface.py
@description: type some description
'''
from abc import ABCMeta, abstractmethod
'''
队列的接口
'''
class Queue_Interface(metaclass=ABCMeta):
    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def enqueue(self, e):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def getFront(self):
        pass
    