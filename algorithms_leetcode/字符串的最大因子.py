'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 00:12:10
@LastEditTime: 2020-03-12 09:36:14
@FilePath: /Algorithms_Note/algorithms_leetcode/字符串的最大因子.py
@description: type some description
'''
'''
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，
我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

示例 3：
输入：str1 = "LEET", str2 = "CODE"
输出：""

提示：
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母
'''
class Solution(object):
    # 时间和空间效率太低了！！！！！
    def gcdOfStrings1(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            return self.helper(str2, str1)
        elif len(str1) > len(str2):
            return self.helper(str1, str2)
        else:
            if str1 == str2:
                return str1
            else:
                return ""
    def helper1(self, l_str, s_str):
        l = len(l_str)
        s = len(s_str)
        if l_str == s_str * (l // s):
            return s_str
        else:
            for i in range(s - 1):
                tem_len = len(s_str[:s-1-i])
                if l_str == s_str[:s-1-i] * (l // tem_len) and s_str == s_str[:s-1-i] * (s // tem_len) :
                    return s_str[:s-1-i]
            return ""
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd_value = math.gcd(len(str1), len(str2))
        tem = str1[:gcd_value]
        if str1 == tem * (len(str1) // len(tem)) and str2 == tem * (len(str2) // len(tem)):
            return tem
        return " "
import math
print(math.gcd(9,12))
    
