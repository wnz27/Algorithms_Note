'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-15 15:10:18
@LastEditTime: 2020-03-15 15:10:40
@FilePath: /Algorithms_Note/其他面试题目/移动零.py
@description: type some description
'''
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1
        return nums