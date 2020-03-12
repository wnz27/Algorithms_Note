'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-07 07:13:34
@LastEditTime: 2020-03-11 09:09:32
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/队列最大值.py
@description: type some description
'''
'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
'''
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
        from collections import deque
        self.s1 = deque()  # 放最大值
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
