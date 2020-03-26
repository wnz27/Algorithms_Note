'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 16:09:04
@LastEditTime: 2020-03-25 16:18:02
@FilePath: /Algorithms_Note/content/其他面试题目/三维形体的表面积.py
@description: type some description
'''
'''
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。
示例 1：
输入：[[2]]
输出：10
示例 2：
输入：[[1,2],[3,4]]
输出：34
示例 3：
输入：[[1,0],[0,2]]
输出：16
示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
'''
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        N = len(grid)
        res = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    res += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            tmp = grid[nr][nc]
                        else:
                            tmp = 0 
                        res += max(grid[r][c] - tmp, 0)
        return res