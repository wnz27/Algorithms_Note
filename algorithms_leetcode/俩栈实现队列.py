'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-05 01:36:46
@LastEditTime: 2020-03-05 01:37:20
@FilePath: /Algorithms_Note/algorithms_practice/俩栈实现队列.py
@description: type some description
'''
'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
 

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
'''
class CQueue(object):
    
    def __init__(self):
        self.s1 = []
        self.s2 = []


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.s1.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.s2 != []:
            return self.s2.pop()
        else:
            if self.s1 == []:
                return -1
            else:
                while self.s1 != []:
                    self.s2.append(self.s1.pop())
                return self.s2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()