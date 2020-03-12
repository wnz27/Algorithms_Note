'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-10 08:57:19
@LastEditTime: 2020-03-10 10:28:36
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/二维数组中的查找.py
@description: type some description
'''
'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。 
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
'''
class Solution(object):
    # 左下角
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 这里如果matrix是空，则i会变成-1，进不去循环直接返回的是False
        i, j = len(matrix)-1, 0
        while i >=0 and j < len(matrix[0]):
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: i -= 1
            else: j += 1
        return False
    # 右上角,细节是魔鬼啊！！！！！！！
    def findNumberIn2DArray2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 而这里如果不判断matrix是否为空，则有可能找列索引时越界
        # 这里：len(matrix[0])-1 产生这样的错
        # IndexError: list index out of range
        if matrix == []:
            return False
        i, j = 0, len(matrix[0])-1
        while j >= 0 and i < len(matrix):
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1
        return False

        
