# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/3/15 21:31
# @Author    : 27
# @File    : rotate_metrix.py

"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 转置旋转矩阵法
        res = []
        while matrix:
            res += matrix.pop(0)
            print("res:", res)
            matrix = list(zip(*matrix))[::-1]
            print("matrix:", matrix)
        return res

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 遍历法
        if not matrix:
            return []
        left, right, top, bottom, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []

        while True:
            # 从左到右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            # 从上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            # 从右到左
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break

            # 从下到上
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res


if __name__ == '__main__':
    a = [[4, 5, 6], [7, 8, 9]]
    print(list(zip(*a))[::-1])
    pass