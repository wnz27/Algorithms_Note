'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-06 12:31:07
@LastEditTime: 2020-03-08 19:15:03
@FilePath: /Algorithms_Note/algorithms_leetcode/N皇后.py
@description: type some description
'''

'''
columnPositions，是一个数组，存放保安位置，索引是保安所在行，值是保安所在列
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.helper([-1]*n, 0, n, res)
        return res
    def helper(self, columnPositions, rowIndex, n, l):     # 辅助方法
        if rowIndex == n:                               # 如果检查完所有行，则输出
            res = self.printSolution(columnPositions, n)
            l.append(res)
            return
        for column in range(n):
            columnPositions[rowIndex] = column          # 每一行每个位置都要试一下
            if self.is_invalid(columnPositions, rowIndex):      # 该行的保安位置是否合理
                self.helper(columnPositions, rowIndex+1, n, l)     # 如果合理，则看剩下行的保安位置情况

    def is_invalid(self, columnPositions, rowIndex):    # 检查插入到rowIndex这行的保安位置是否合理
        for i in range(rowIndex):
            if columnPositions[i] == columnPositions[rowIndex]: # 如果有同列的情况
                return False
            if abs(columnPositions[i] - columnPositions[rowIndex]) == rowIndex - i:  # 如果有在斜线情况
                return False
        return True
    def printSolution(self, columnPositions, n):        # 打印结果
        tem = []
        for row in range(n):
            line = ''
            for col in range(n):
                if columnPositions[row] == col:
                    line += 'Q '
                else:
                    line += '. '
            print(line)
            tem.append(line)
        print('--' * n)
        return tem
s = Solution()
print(s.solveNQueens(5))
