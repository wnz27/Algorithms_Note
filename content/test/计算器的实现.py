from typing import List

'''
计算器的计算实现
'''


def calculate(s: str) -> int:
    def helper(string_list: List[str]) -> int:
        stack = []
        sign = '+'
        num = 0
        while len(string_list) > 0:
            c = string_list.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num 
            if c == '(':
                num = helper(string_list)
            if (not c.isdigit() and c != ' ') or len(string_list) == 0:
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


if __name__ == '__main__':
    print(list('10 * ( 5+4*6) - 6+7'))
    pass
