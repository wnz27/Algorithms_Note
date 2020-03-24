'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-24 10:58:41
@LastEditTime: 2020-03-24 11:18:11
@FilePath: /Algorithms_Note/content/其他面试题目/存在重复.py
@description: type some description
'''
'''
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false
示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''
class Solution(object):
    # 时间On，空间On
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        helper = collections.Counter(nums)
        for count in helper.values():
            if count > 1:
                return True
        return False

    # 时间Nlongn，空间O1
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
            for i in range(len(nums)-1):
                if nums[i] == nums[i + 1]:
                    return True
            return False
s = Solution()
a = s.containsDuplicate([0])
print(a)
