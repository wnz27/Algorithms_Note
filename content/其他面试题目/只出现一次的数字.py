'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-24 11:59:19
@LastEditTime: 2020-03-24 13:19:27
@FilePath: /Algorithms_Note/content/其他面试题目/只出现一次的数字.py
@description: type some description
'''
'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
'''
class Solution(object):
    # 排序
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2:
            return nums[0]
        nums.sort()
        slow, fast = 0,1
        while fast < l:
            if nums[slow] != nums[fast]:
                return nums[slow]
            if fast == l-2:
                return nums[-1]
            slow += 2
            fast += 2
            
    # 哈希
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        helper = collections.Counter(nums)
        for k, v in helper.items():
            if v == 1:
                return k

    # 数学
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        2 (a + b + c) - (a + b + b + c + c) = a
        '''
        return 2 * sum(set(nums)) - sum(nums)

    # 异或
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i range(1, len(nums)):
            res ^= nums[i]
        return res