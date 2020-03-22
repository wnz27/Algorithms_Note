'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 15:27:51
@LastEditTime: 2020-03-13 15:41:19
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/18包含min的栈.py
@description: type some description
'''
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

提示：
各函数的调用总次数不超过 20000 次
'''
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        self.__mini = []


    def push(self, x):
        self.__data.append(x)
        if not self.__mini or x <= self.__mini[-1]:
            self.__mini.append(x)

    def pop(self):
        if self.__mini[-1] >= self.top():
            self.__mini.pop()
        self.__data.pop()

    def top(self):
        return self.__data[-1]


    def min(self):
        return self.__mini[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()