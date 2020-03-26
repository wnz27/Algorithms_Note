'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 18:04:58
@LastEditTime: 2020-03-25 18:23:49
@FilePath: /Algorithms_Note/content/其他面试题目/两数之和.py
@description: type some description
'''
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution(object):
    # 哈希
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        helper = {}
        for i in range(len(nums)):
            if target-nums[i] in helper:
                return [helper[target-nums[i]], i]
            helper[nums[i]] = i
        return -1
s = Solution()
a = s.twoSum([2, 7, 11, 15], 9)
print(a)