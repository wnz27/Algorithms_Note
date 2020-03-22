'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-03 00:11:27
@LastEditTime: 2020-03-03 00:29:31
@FilePath: /Algorithms_Note/algorithms_practice/合并排序数组.py
@description: type some description
'''
'''
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 
编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。

示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        # 方法一，把B拷贝进A，然后原地排序
        for i in range(n):
            A[i + m] = B[i]
        A.sort()
    # 暂时没想到方法二
    def merge2(self, A, m, B, n):
        pass
