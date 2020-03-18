'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-18 10:36:42
@LastEditTime: 2020-03-18 10:55:12
@FilePath: /Algorithms_Note/其他面试题目/验证回文串.py
@description: type some description
'''
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i, j = 0, l-1
        while i < j:
            while i < l and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
