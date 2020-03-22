'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 01:47:35
@LastEditTime: 2020-03-14 11:40:19
@FilePath: /Algorithms_Note/其他面试题目/最长上升子序列.py
@description: type some description
'''
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = []     # d[i]是以第i个元素结尾的最长上升子序列长度
        for i in range(len(nums)):
            dp.append(1)    # 自己天然是一个子序列
            for j in range(i):
                if nums[i] > nums[j]:   # 只有大于前面的值，才构成增(上升)序列
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)



        