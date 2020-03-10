'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-08 23:11:49
@LastEditTime: 2020-03-09 00:25:40
@FilePath: /Algorithms_Note/test/ttt.py
@description: type some description
'''
'''
计算器的计算实现
'''
def calculate(s: str) -> int:
    def helper(s: list) -> int: 
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0: 
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num 
            if c == '(':
                num = helper(s)
            if (not c.isdigit() and c != ' ') or len(s) == 0: 
                if sign == '+':
                    stack.append(num) 
                elif sign == '-':
                    stack.append(-num) 
                elif sign == '*':
                    stack[-1] = stack[-1] * num 
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = stack[-1] // float(num)
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ')': 
                break
        return sum(stack)
    return helper(list(s))
print(calculate('10 * ( 5+4*6) - 6+7'))