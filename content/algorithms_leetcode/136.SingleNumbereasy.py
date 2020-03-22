# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        #此方法执行时间超出
        for i in nums:
            if nums.count(i) == 1:
                return i
            else:
                continue
        '''

        tem = []
        tem[0] = nums[0]
        for i in nums:
            if i