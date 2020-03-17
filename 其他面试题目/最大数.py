'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 12:31:14
@LastEditTime: 2020-03-16 00:33:37
@FilePath: /Algorithms_Note/其他面试题目/最大数.py
@description: type some description
'''
'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210
示例 2:
输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
