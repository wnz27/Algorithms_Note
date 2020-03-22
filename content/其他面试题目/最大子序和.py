'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 08:48:05
@LastEditTime: 2020-03-14 09:13:22
@FilePath: /Algorithms_Note/其他面试题目/最大子序和.py
@description: type some description
'''
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
class Solution(object):
    # 能输出起始位置的：
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        sum_n = 0
        maxi = nums[0]
        for i in range(len(nums)):
            sum_n += nums[i]
            if nums[i] > sum_n:
                start = i
                sum_n = nums[i]
            if sum_n > maxi:
                maxi = sum_n
                end = i
        return maxi
    # 不输出起始位置的:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        sum_n = 0
        for i in nums:
            sum_n += i
            if sum_n < i:
                sum_n = i
            if sum_n > maxi:
                maxi = sum_n
        return maxi