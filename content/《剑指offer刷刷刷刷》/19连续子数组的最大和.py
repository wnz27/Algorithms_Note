'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 15:54:05
@LastEditTime: 2020-03-13 16:28:55
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/19连续子数组的最大和.py
@description: type some description
'''
'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
# 动态规划
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 只返回最大值
        curr_sum = 0
        maxi = nums[0]
        for i in nums:
            curr_sum += i
            if curr_sum < i:
                curr_sum = i
            if curr_sum > maxi:
                maxi = curr_sum
        return maxi

    # 不但输出最大，还可找出起止位置
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        tmp = 0 
        maxi = nums[0]
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp < nums[i]:
                tmp = nums[i]
                start = i
            if tmp > maxi:
                maxi = tmp
                end = i
        return maxi
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

