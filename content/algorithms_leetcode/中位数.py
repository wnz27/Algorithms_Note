# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/11 11:39 上午
from typing import List


"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
 

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

"""


class Solution:
    def merge_num_list(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ O(n) """
        if not nums1 and not nums2:
            return []
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        p1 = 0
        p2 = 0
        merge_list = []
        len1 = len(nums1)
        len2 = len(nums2)
        while p1 <= len1 - 1 or p2 <= len2 - 1:
            if p1 == len1:
                n1 = float("inf")
            else:
                n1 = nums1[p1]
            if p2 == len2:
                n2 = float("inf")
            else:
                n2 = nums2[p2]
            if n1 < n2:
                merge_list.append(n1)
                p1 += 1
            else:
                merge_list.append(n2)
                p2 += 1
        return merge_list

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = self.merge_num_list(nums1, nums2)
        if not merge_list:
            return 0
        length = len(merge_list)
        middle_idx = int(length / 2)
        middle_value = float(merge_list[middle_idx])
        if length % 2 == 0:
            idx2 = middle_idx - 1
            n2 = merge_list[idx2]
            number = middle_value + n2
            return number / 2
        else:
            return middle_value


if __name__ == '__main__':
    s = Solution()
    a = [1, 3]
    b = [2, 4]
    res = s.findMedianSortedArrays(a, b)
    print(res)
    pass
