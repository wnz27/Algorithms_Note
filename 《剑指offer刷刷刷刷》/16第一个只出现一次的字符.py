'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 10:51:58
@LastEditTime: 2020-03-12 11:45:12
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/16第一个只出现一次的字符.py
@description: type some description
'''
'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:
s = "abaccdeff"
返回 "b"
s = "" 
返回 " "
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """