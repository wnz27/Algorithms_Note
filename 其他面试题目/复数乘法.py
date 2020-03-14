'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 11:43:06
@LastEditTime: 2020-03-14 12:05:17
@FilePath: /Algorithms_Note/其他面试题目/复数乘法.py
@description: type some description
'''
'''
给定两个表示复数的字符串。
返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
注意:

输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。
输出也应当符合这种形式。
'''
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = a.split("+")
        b1 = b.split("+")
        real = int(a1[0]) * int(b1[0]) + (- (int(a1[1][:-1]) * int(b1[1][:-1])))
        virtual = int(a1[0]) * int(b1[1][:-1]) + int(a1[1][:-1]) * int(b1[0])
        return str(real) + "+" + str(virtual) + "i"