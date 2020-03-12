'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 00:08:17
@LastEditTime: 2020-03-12 11:44:52
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/13调整数组顺序使奇数在偶数前面.py
@description: type some description
'''
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
'''
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        