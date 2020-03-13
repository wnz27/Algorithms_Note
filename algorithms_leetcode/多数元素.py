'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 07:08:56
@LastEditTime: 2020-03-13 07:50:34
@FilePath: /Algorithms_Note/algorithms_leetcode/多数元素.py
@description: type some description
'''
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''
class Solution:
    # 时间复杂度低，空间复杂度高
    def majorityElement1(self, nums):
        helper = {}
        count = len(nums) // 2
        for i in nums:
            if i in helper:
                helper[i] += 1
            helper.setdefault(i, 1)
        max_freq = max(helper, lambda:x helper[x])
    # 众数方法，排序后，n/2的位置众数一定能覆盖到
    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    # 众数候选者法：
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        return candidate