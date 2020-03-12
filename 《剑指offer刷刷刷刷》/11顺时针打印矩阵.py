'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 21:11:36
@LastEditTime: 2020-03-11 23:21:54
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/顺时针打印矩阵.py
@description: type some description
'''
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''
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
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):       # 从左到右
                res.append(matrix[t][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1):         # 从上到下
                res.append(matrix[i][r])
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1):   # 从右到左
                res.append(matrix[b][i])
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1):   # 从下到上
                res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res

# 再次！！！细节是魔鬼！！！！！细节是魔鬼！！！！！细节是魔鬼！！！！！
# t>b 以及 l>r 加上=号的话会提前终止，少输出！！！！！！

s = Solution()
s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])