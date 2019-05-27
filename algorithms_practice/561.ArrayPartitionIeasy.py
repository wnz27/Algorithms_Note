# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

分析可知，只有按顺序排列之后，每两个做一组取最小值得到的和是最大的，如果每组取两端，那么相当于前一半的和，没有每两个一组取最小值后的和大。
'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        sortList = sorted(nums)
        for index in range(len(sortList)):
            if index%2 == 0:
                result += sortList[index]
            else:
                continue
        return result
