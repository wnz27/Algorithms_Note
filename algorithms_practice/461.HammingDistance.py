# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。例如：
1011101 与 1001001 之间的汉明距离是 2。
2143896 与 2233796 之间的汉明距离是 3。
"toned" 与 "roses" 之间的汉明距离是 3。

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num1 = self.sameLen(x,y)[0]
        num2 = self.sameLen(x,y)[1]
        hamingD = 0
        for index in range(len(num1)):
            if num1[index] != num2[index]:
                hamingD += 1
            else:
                continue
        return hamingD
    
    def sameLen(self,intx,inty):
        '''
        将两个数字变成二进制数，然后变成一样长
        返回包含两个字符串的列表，被增加的在后。
        '''
        x = format(intx,"b")
        y = format(inty,"b")
        result = []
        if len(x) > len(y):
            result.append(x)
            result.append("0"*(len(x)-len(y)) + y)
            return result
        else:
            result.append(y)
            result.append("0"*(len(y)-len(x)) + x)
            return result
        

        


