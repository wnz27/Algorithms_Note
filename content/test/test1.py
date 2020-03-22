'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-07 11:57:40
@LastEditTime: 2020-03-07 15:07:08
@FilePath: /Algorithms_Note/test/test1.py
@description: type some description
'''
import queue
class MaxQueue(object):
    class LoopQueue:
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
                index = (index + 1) % len(self.__data)
            return '{}, size: {}, capacity: {}'.format(res, self.__size, self.getCapacity)

    def __init__(self):
        self.s1 = queue.deque() # 放最大值
        self.s2 = self.LoopQueue()  # 放实际数据


    def max_value(self):
        """
        :rtype: int
        """
        return self.s1[0] if self.s1 else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.s1 and self.s1[-1] < value:
            self.s1.pop()
        self.s1.append(value)
        self.s2.enqueue(value)
            

    def pop_front(self):
        """
        :rtype: int
        """
        if self.s2.isEmpty():
            return -1
        else:
            if self.s1[0] == self.s2.getFront():
                self.s1.popleft()
        return self.s2.dequeue()

m = MaxQueue()
m.push_back(1)
print(m.s1, m.s2)
m.push_back(2)
print(m.s1, m.s2)
m.push_back(1)
print(m.s1, m.s2)
m.push_back(10)
print(m.s1, m.s2)
m.push_back(2)
print(m.s1, m.s2)
m.push_back(4)
m.pop_front()
m.pop_front()
print(m.s1, m.s2)
m.pop_front()
print(m.s1, m.s2)
m.pop_front()
print(m.s1, m.s2)
print(m.max_value())
print(m.pop_front())
print(m.max_value())