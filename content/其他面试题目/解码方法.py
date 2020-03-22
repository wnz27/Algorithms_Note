'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 23:57:35
@LastEditTime: 2020-03-18 02:00:07
@FilePath: /Algorithms_Note/其他面试题目/解码方法.py
@description: type some description
'''
'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith("0"):
            return 0
        l = len(s)
        dp = [0] * (l + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, l):
            tem = int(s[i-1]) * 10 + int(s[i])
            if int(s[i]) > 0:
                dp[i + 1] = dp[i]
            if tem > 9 and tem <= 26:
                dp[i + 1] += dp[i - 1]
            if dp[i + 1] == 0: return 0
        return dp[l]
