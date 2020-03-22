'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-18 10:36:58
@LastEditTime: 2020-03-18 11:38:01
@FilePath: /Algorithms_Note/其他面试题目/验证回文串II.py
@description: type some description
'''
'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
输入: "aba"
输出: True
示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i, j = 0, l - 1
        while i < j:
            if s[i] != s[j]:
                # 舍弃左边字符
                a = s[i + 1:j + 1]
                # 舍弃右边字符
                b = s[i:j]
                return a == a[::-1] or b == b[::-1]
            else:
                i += 1
                j -= 1
        return True