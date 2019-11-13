#! -*- encoding=utf-8 -*-
# 数组实现，未加锁，线程不安全
class MyCircularQueue(object):
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.length = k
        self.queue = []
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.length:
            self.queue.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return False
        else:
            self.queue.pop(self.queue[0])
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[len(self.queue)-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if len(self.queue) == self.length:
            return True
        else:
            False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_7 = obj.enQueue(2)
param_8 = obj.enQueue(3)
param_9 = obj.enQueue(4)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
print(param_1)
print(param_7)
print(param_8)
print(param_9)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
