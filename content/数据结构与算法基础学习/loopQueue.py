'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-02 18:24:35
@LastEditTime: 2020-03-21 19:34:25
@FilePath: /Algorithms_Note/数据结构与算法基础学习/loopQueue.py
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
    
class LoopQueue(Queue_Interface):
    def __init__(self, capacity = 10):
        self.__data = [None] * (capacity + 1)
        self.__size = 0
        '''
        没有size变量的话求size的方法如下：
        （capacity - 头指针值）% capacity + 尾指针值
        '''
        self.__front = 0
        self.__tail = 0
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__front == self.__tail
    
    @property
    def getCapacity(self):
        return len(self.__data) - 1
    
    def enqueue(self, e):
        if (self.__tail + 1) % len(self.__data) == self.__front:
            self.resizeloopQueue(2 * self.getCapacity)
        self.__data[self.__tail] = e
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Cannot dequeue element from an empty queue.')
        res = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        if self.__size == int(self.getCapacity / 4) and int(self.getCapacity/2) != 0:
            self.resizeloopQueue(int(self.getCapacity/2))
        return res
    
    def getFront(self):
        if self.isEmpty():
            raise IndexError('Cannot get element from an empty queue.')
        return self.__data[self.__front]
    
    def getLast(self):
        if self.isEmpty():
            raise IndexError('Cannot get element from an empty queue.')
        if self.__tail == 0:
            index = self.__size - 1
        else:
            index = self.__tail - 1
        return self.__data[index]
    
    def removeLast(self):
        if self.isEmpty():
            raise IndexError('Cannot remove element from an empty queue.')
        if self.__tail == 0:
            index = self.__size - 1
        else:
            index = self.__tail - 1
        self.__data[self.__tail] = None
        self.__tail = index
        self.__size -= 1

    def resizeloopQueue(self, newLength):
        newData = [None] * (newLength + 1)
        for i in range(self.__size):     # 第一种遍历循环列表的方式
            newData[i] = self.__data[(i+self.__front)%len(self.__data)]
        self.__data = newData
        self.__front = 0
        self.__tail = self.__size

    def __str__(self):
        index = self.__front
        res = 'loopQueue front: ['
        while index != self.__tail:     # 第二种遍历循环列表的方式
            res += str(self.__data[index])
            if (index + 1) % len(self.__data) != self.__tail:
                res += ', '
            else:
                res += '] tail'
            index = (index + 1) % len(self.__data)      # 关键点
        return '{}, size: {}, capacity: {}'.format(res, self.__size, self.getCapacity)

lq = LoopQueue(4)
lq.enqueue(1)
print(lq)
lq.enqueue(2)
print(lq)
lq.enqueue(99)
print(lq)
a= lq.getFront()
print( a)
lq.enqueue(1002000100)
print(lq)
lq.enqueue(5647)
print(lq)