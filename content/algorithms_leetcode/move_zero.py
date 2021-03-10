# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/10 2:49 下午
from typing import List


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1


if __name__ == '__main__':
    """
    输入: [2,1,0,3,12]
    输出: [2,1,3,12,0]    
    """
    pass
