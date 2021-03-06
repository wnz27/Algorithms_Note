'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-24 13:28:48
@LastEditTime: 2020-03-25 16:37:30
@FilePath: /Algorithms_Note/content/其他面试题目/两个数组的交集.py
@description: type some description
'''
'''
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
import collections
class Solution(object):
    # 哈希
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        helper = collections.Counter(nums1)
        for num in nums2:
            if helper.get(num, 0):
                helper[num] -= 1
                res.append(num)
        return res

    # 排序
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

    # 省内存方法
    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        pass

        
