'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 17:33:43
@LastEditTime: 2020-03-25 17:52:42
@FilePath: /Algorithms_Note/content/其他面试题目/移动0.py
@description: type some description
'''
'''
移动零
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
        l = len(nums)
        i = 0
        for j in range(l):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


