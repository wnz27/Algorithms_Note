# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/4/2 00:04
# @Author    : 27
# @File    : 笨阶乘.py
"""
1006. 笨阶乘
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。

相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。

实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
"""
import math


class Solution:
    signs = ["*", "/", "+", "-"]
    def clumsy(self, N: int) -> int:
        cal_stack = [N]
        op = 0
        for i in range(1, N):
            sign = self.signs[op]
            print(sign)
            curr_value = N - i
            print(curr_value)
            if sign == "*":
                cal_stack.append(cal_stack.pop() * curr_value)
            elif sign == "/":
                cal_stack.append(int(cal_stack.pop() / float(curr_value)))
            elif sign == "+":
                cal_stack.append(curr_value)
            else:
                cal_stack.append(0 - curr_value)
            op = (op + 1) % 4
        return sum(cal_stack)

if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(10))
    pass
