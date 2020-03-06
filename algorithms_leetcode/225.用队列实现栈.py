'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-01 16:29:35
@LastEditTime: 2020-03-02 09:45:28
@FilePath: /Algorithms_Note/algorithms_practice/225.用队列实现栈.py
@description: type some description
'''
# 方法一，时间复杂度, pushO(1), popO(n)
class MyStack1(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__q1 = []
        self.__q2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.__q1.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.__q1) > 1:
            self.__q2.append(self.__q1.pop(0))
        res = self.__q1.pop()
        self.__q1, self.__q2 = self.__q2, self.__q1
        return res


    def top(self):  # O1
        """
        Get the top element.
        :rtype: int
        """
        if len(self.__q1) != 0:
            return self.__q1[-1]
        else:
            return -1


    def empty(self):  # O1
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.__q1 == [] and self.__q2 == []


# 方法二，时间复杂度, pushO(n), popO(1)
class MyStack2(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q2.insert(0, x)
        while len(self.q1) != 0:
            self.q2.insert(0, self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.pop() 


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1 == []

# 方法三，单队列实现，时间复杂度, pushO(n), popO(1)
class MyStack3(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__q = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.__q.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.__q.pop()
        


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.__q[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.__q == []


