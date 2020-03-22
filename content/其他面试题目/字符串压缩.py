'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-16 08:01:38
@LastEditTime: 2020-03-16 08:02:12
@FilePath: /Algorithms_Note/其他面试题目/字符串压缩.py
@description: type some description
'''
'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
你可以假设字符串中只包含大小写英文字母（a至z）。
示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：
字符串长度在[0, 50000]范围内。
'''
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        length = len(S)
        count = 1
        res = ''
        for i in range(1, length):
            if S[i] == S[i-1]:
                count += 1
            else:
                res += S[i-1] + str(count)
                count = 1
        res += S[length-1] + str(count)
        return res if len(res) < length else S