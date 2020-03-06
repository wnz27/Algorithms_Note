'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-05 09:52:34
@LastEditTime: 2020-03-06 09:25:20
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/和为s的连续正数序列.py
@description: type some description
'''
'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
'''
class Solution(object):
    # 空间复杂度o1，时间太差
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = int(target/2)
        for i in range(1,l+1):
            line = []
            line.append(i)
            while sum(line) < target:
                line.append(i + 1)
                i += 1  # 确保加入的是连续的递增正数
                if sum(line) == target:
                    res.append(line)
                elif sum(line) < target:
                    continue
                else:  # sum(line) > target
                    break
        return res
    # 优化时间复杂度
    def findContinuousSequence2(self, target):
        """
    :type target: int
    :rtype: List[List[int]]
    """
        res = []
        n = int(target/2) + 1  # 只用遍历一半
        line = [i for i in range(1,n+1)]
        print(line)
        p, q = 0, 0 # 快慢指针
        while q < n and p < n:  # 只要有一个越界，查找就结束了，也就找全了，思考边界情况
            num = sum(line[q:p+1])
            if num < target:
                # if q == n-1:  # 防止最后一个数小于target陷入死循环
                #     break
                p += 1
                continue
            elif num == target:
                res.append(line[q:p+1])
                print('res', res)
                p += 1
            q += 1
        return res

s = Solution()
s.findContinuousSequence(9)
print(s.findContinuousSequence2(15))
