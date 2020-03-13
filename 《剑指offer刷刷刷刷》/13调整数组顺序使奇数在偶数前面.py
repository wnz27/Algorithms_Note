'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 00:08:17
@LastEditTime: 2020-03-13 15:53:10
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/13调整数组顺序使奇数在偶数前面.py
@description: type some description
'''
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
'''
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 双指针
        head, tail = 0, len(nums) - 1
        while head < tail:
            if nums[head] % 2 == 0 and nums[tail] % 2 == 1:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1
            else:
                if nums[head] % 2 == 0:     # 尾指针所指的数已经是偶数
                    tail -= 1
                elif nums[tail] % 2 == 1:   # 头指针指的数已经是奇数
                    head += 1
                else:   # 尾指针所指的数已经是偶数且头指针指的数已经是奇数
                    head += 1
                    tail -= 1
        return nums
        


        