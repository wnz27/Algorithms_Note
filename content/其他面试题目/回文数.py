'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 10:08:57
@LastEditTime: 2020-03-14 11:00:25
@FilePath: /Algorithms_Note/其他面试题目/回文数.py
@description: type some description
'''
'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
'''
class Solution(object):
    # 使用字符
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 使用字符串
        s = str(x)
        h, t = 0, len(s) - 1
        while h < t:
            if s[h] != s[t]:
                return False
            h += 1
            t -= 1
        return True
    # 不使用字符
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 不使用字符
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        res = []
        while x != 0:
            x, need = divmod(x, 10)
            res.append(need)
        start, end = 0, len(res) - 1
        while start < end:
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        return True

    # 不使用字符
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # // 特殊情况：
        # // 如上所述，当 x < 0 时，x 不是回文数。
        # // 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # // 则其第一位数字也应该是 0
        # // 只有 0 满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10

        # // 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        # // 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        # // 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == revertedNumber || x == revertedNumber/10