'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 17:04:07
@LastEditTime: 2020-03-21 20:19:39
@FilePath: /Algorithms_Note/其他面试题目/最长回文串.py
@description: type some description
'''
'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。
示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        import collections
        tem = collections.Counter(s)        # On
        c = 0  # 记录单数的字符种类数
        for v in tem.values():              # On
            if v % 2 == 1:
                c += 1
        if c <= 1:
            return l
        else:
            return l - c + 1  # 单数字符最多存在一个
        


