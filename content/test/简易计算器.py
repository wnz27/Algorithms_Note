# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/3/11 03:25
# @File    : 简易计算器.py

"""
def calculate(self , s):
        # 初始化sign为 “+”，是因为开头是数字
        num ,stack ,sign = 0 , [] , '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            #根据当前数字之前的符号，来决定如何处理当前数值
            # 并将处理后的数值压入栈中
            if ch in "+-*/" or i == len(s)-1:
                if sign == "+" :
                    stack.append(num)
                elif sign == "-" :
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = ch
        return sum(stack)
"""
"""
超出时间限制：
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        string_list = list(s)
        sign = "+"
        while len(string_list) > 0:
            curr_str = string_list.pop(0)
            if curr_str.isdigit():
                num = num * 10 + int(curr_str)
            if (not curr_str.isdigit() and curr_str != " ") or len(string_list) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
                sign = curr_str
                num = 0
        return sum(stack)
"""

