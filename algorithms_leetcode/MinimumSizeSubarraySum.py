'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-29 18:38:34
@LastEditTime: 2020-02-29 18:55:43
@FilePath: /Algorithms_Note/algorithms_practice/ MinimumSizeSubarraySum.py
@description: type some description
'''
'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
# 暴力法
# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n < 1:
#             return 0
#         for i in range(1,n+1):
#             tem = self.helper(i, nums, s)
#             if tem:
#                 return tem[1] - tem[0]
#             else:
#                 continue
#         return 0
            
        
#     def helper(self, n, nums, target):
#         '''
#         rtype:(slow,fast) or None
#         '''
#         l = len(nums)
#         slow = 0
#         fast = slow + n
#         while fast <= l:
#             print("llll",sum(nums[slow:fast]))
#             if sum(nums[slow:fast]) >= target:
#                 return (slow, fast)
#             slow += 1
#             fast += 1
#         return None

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        pass

s = Solution()
print(s.minSubArrayLen(15, [1,2,3,4,5]))