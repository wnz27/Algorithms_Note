# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/3/16 21:34
# @Author    : 27
# @File    : rotate_metrix2.py
"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            print("row:{}, col:{}".format(row, col), matrix[row][col])
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
        return matrix

    def generateMatrix2(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                    print(bottom, col, num)
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
                    print(row, left, num)

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix

    def tttt(self, n):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, right, bottom, left = 0, n - 1, n - 1, 0

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return matrix

    def generateMatrix3(self, n: int) -> List[List[int]]:
        target_number = n * n
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col, dir_index = 0, 0, 0
        metrix = [[0] * n for _ in range(n)]
        for i in range(target_number):
            metrix[row][col] = i + 1
            # print("row:{}, col:{}".format(row, col), metrix[row][col])

            dx, dy = dirs[dir_index]
            # 验证下一个方向正确性
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or metrix[r][c] > 0:
                # 如果不正确则修正方向
                dir_index = (dir_index + 1) % 4
                dx, dy = dirs[dir_index]
            # 给定正确的行列
            row, col = row + dx, col + dy
            # print(row, col)
        return metrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix2(3))
    pass

