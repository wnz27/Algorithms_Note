'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-17 22:58:36
@LastEditTime: 2020-03-17 23:43:39
@FilePath: /Algorithms_Note/其他面试题目/字符串相乘.py
@description: type some description
'''
'''
给定两个以字符串形式表示的非负整数 num1 和 num2，
返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return "0"
        l = len(num1) + len(num2)
        res = [0] * l
        for i in range(len(num1)):      # 被乘数
            for j in range(len(num2)):  # 乘数
                tem = int(num1[i]) * int(num2[j])
                n1, n2 = divmod(tem, 10)
                if tem >= 10:
                    res[i + j] += n1
                    res[i + j + 1] += n2
                else:
                    res[i+ j + 1] += tem
        carry = 0
        for i in range(l-1, -1, -1):
            curr_val = carry + res[i]
            n1, n2 = divmod(curr_val, 10)
            if curr_val >= 10:
                carry = n1
                res[i] = n2
            else:
                res[i] = curr_val
                carry = 0
        for i in range(l):
            res[i] = str(res[i])
        return ''.join(res).lstrip("0")
s = Solution()
a = s.multiply("999","999")
print(a)