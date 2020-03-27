'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-26 11:05:02
@LastEditTime: 2020-03-26 17:48:37
@FilePath: /Algorithms_Note/content/其他面试题目/旋转图像.py
@description: type some description
'''
'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
class Solution(object):
    # 先转置，再翻转
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # 矩阵转置
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # 矩阵每行翻转
        for i in range(N):
            matrix[i].reverse()
    # 移位法
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 每次移位4个数
        N = len(matrix)
        for i in range(N//2 + N%2):         # 所以相当于给矩阵划分为四个部分，只需要遍历左上角的那一块区域
            for j in range(N//2):
                tmp = matrix[N-j-1][i]
                matrix[N-j-1][i] = matrix[N-i-1][N-j-1]
                matrix[N-i-1][N-j-1] = matrix[j][N-i-1]
                matrix[j][N-i-1] = matrix[i][j]
                matrix[i][j] = tmp
    # 与上面方法有细微差别
    def rotate3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 每次移位4个数
        N = len(matrix)
        for i in range(N//2):         # 所以相当于给矩阵划分为四个部分，只需要遍历左上角的那一块区域
            for j in range(N//2 + N%2):
                tmp = matrix[N-j-1][i]
                matrix[N-j-1][i] = matrix[N-i-1][N-j-1]
                matrix[N-i-1][N-j-1] = matrix[j][N-i-1]
                matrix[j][N-i-1] = matrix[i][j]
                matrix[i][j] = tmp
