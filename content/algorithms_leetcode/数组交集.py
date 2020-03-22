'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-04 18:10:13
@LastEditTime: 2020-03-04 18:30:10
@FilePath: /Algorithms_Note/algorithms_practice/数组交集.py
@description: type some description
'''
'''
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
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        helper = {}
        for i in nums1:   # 构造字典
            if i in helper:
                helper[i] += 1
            else:
                helper[i] = 1
        for i in nums2:
            if i in helper:  # 如果某个数在字典里，说明出现了重复
                if helper[i] == 0:  # 如果字典里这个数的频数是0
                    helper.pop(i)   # 则说明不能加到结果里，把字典这个key删掉
                    continue               # 并且进入下一个循环
                res.append(i)       # 如果这个数的频数不为0，则说明可以作为一个交集的数字加入结果。
                helper[i] -= 1      # 把字典里的该数对应的频数减一，示意用掉了一个
            else:
                continue
        return res 



            