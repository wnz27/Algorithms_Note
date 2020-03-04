'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-04 08:11:32
@LastEditTime: 2020-03-04 08:53:24
@FilePath: /Algorithms_Note/algorithms_practice/腐烂的橘子.py
@description: type some description
'''
import collections
'''
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))
        diret = [(0,1), (0,-1), (1,0),(-1,0)]
        def genarate_diret(r,c):
            for d in diret:
                if 0 <= c+d[0] < C and 0 <= r+d[1] < R:
                    yield r+d[1], c+d[0]
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in genarate_diret(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))
                    print(queue)
        if any(1 in row for row in grid):
            return -1
        return d

s = Solution()
a = s.orangesRotting(
[[2,1,1],[1,1,0],[0,1,1]])
print(a)

        
        

        