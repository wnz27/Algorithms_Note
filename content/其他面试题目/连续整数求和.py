'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 00:42:51
@LastEditTime: 2020-03-14 01:35:56
@FilePath: /Algorithms_Note/其他面试题目/连续整数求和.py
@description: type some description
'''
'''
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
示例 1:
输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:
输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:
输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
'''
class Solution(object):
    # 超出时间限制
    def consecutiveNumbersSum1(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        count = 1
        n = N // 2 + 1
        sum_n = 0
        res = [(N,N)]
        start, end = 1,0
        for i in range(1, n+1):
            sum_n += i
            if sum_n == N:
                end = i
                res.append((start, end))
            if sum_n > N:
                while sum_n > N:
                    sum_n = sum_n - start
                    start += 1
                if sum_n == N:
                    end = i
                    if start < end:
                        res.append((start, end))
        return len(res)
    # 进阶
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        '''
        # 1个数时，必然有一个数可构成N
        # 2个数若要构成N，第2个数与第1个数差为1，N减掉这个1能整除2则能由商与商+1构成N
        # 3个数若要构成N，第2个数与第1个数差为1，第3个数与第1个数的差为2，N减掉1再减掉2能整除3则能由商、商+1与商+2构成N
        # 依次类推，当商即第1个数小于等于0时结束
        '''
        res, i = 0, 1
        while N > 0:
            res += N % i == 0
            N -= i
            i += 1
        return res
s= Solution()
s.consecutiveNumbersSum(1)