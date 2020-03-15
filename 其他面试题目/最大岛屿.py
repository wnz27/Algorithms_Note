'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-15 08:15:23
@LastEditTime: 2020-03-15 08:16:07
@FilePath: /Algorithms_Note/其他面试题目/最大岛屿.py
@description: type some description
'''
'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 
的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.maxArea = 0        # 存储最大岛屿面积
        if not grid:
            return 0
        row = len(grid)         # 保存地图行数
        col = len(grid[0])      # 保存地图列数
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    current = 1
                    self.dfs(i, j, current, grid)                # 计算岛屿面积，核心逻辑
        return self.maxArea             # 返回最大面积

    def dfs(self, x, y, current, grid):     # x,y 为当前坐标，current为当前岛屿面积，grid为地图
        # 先把搜索的地方做标记
        grid[x][y] = 2
        # 向上搜索
        if x > 0 and grid[x-1][y] == 1:     # 向上走先考察是否越界并且是否为陆地
            current = self.dfs(x-1, y, current+1, grid)
        # 向下搜索
        if x < (len(grid)-1) and grid[x+1][y] == 1:     # 向下走先考虑是否越界且是否为陆地
            current = self.dfs(x+1, y, current+1, grid)
        # 向左搜索
        if y > 0 and grid[x][y-1] == 1:                 # 考虑是否越界与陆地
            current = self.dfs(x, y-1, current+1, grid)
        # 向右搜索
        if y < (len(grid[0])-1) and grid[x][y+1] == 1:      # 考虑是否越界与陆地
            current = self.dfs(x, y+1, current+1, grid)
        self.maxArea = max(self.maxArea, current)       # 更新最大面积变量
        return current

        