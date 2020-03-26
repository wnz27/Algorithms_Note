'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 16:42:37
@LastEditTime: 2020-03-25 17:32:36
@FilePath: /Algorithms_Note/content/其他面试题目/加一.py
@description: type some description
'''
'''
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits))[::-1]:
            val = digits[i] + carry
            if val > 9:
                carry = 1
                digits[i] = val - 10
            else:
                carry = 0
                digits[i] = val
        if carry == 1:
            digits.insert(0,1)
        return digits