#! -*- coding=utf-8 -*-
import time, functools

# 写一个测试函数执行时间的装饰器
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end-start)*1000))
        return res
    return wrapper

# 后面测试函数你就可以看出不同实现对效率的影响有多么大

'''
递归实现
'''
def fib_recursive(n):
    # 递归基，递归出口，退化情况
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_recursive_optimize(n, d):
    # d，一个字典存储调用过的情况
    # 递归基，递归出口，退化情况
    if n <= 1:
        return n
    else:
        if str(n) in d.keys():
            return d[str(n)]
        else:
            cur_fib = fib_recursive_optimize(n-1 , d) + fib_recursive_optimize(n-2, d)
            d[str(n)] = cur_fib
            return cur_fib

@log_execution_time
def test_fib():
    print('测试最差fib递归函数：')
    fib_recursive(30)

@log_execution_time
def test_fib_op():
    print('测试改进版fib递归函数：')
    d = {}
    fib_recursive_optimize(60,d)


test_fib_op()
print('*'*80)
test_fib()

'''
迭代实现
'''
def fib_generate(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# 等价方法
def fib_ge(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
    return b
# print(fib_generate(0))
# print(fib_generate(1))
# print(fib_generate(2))
# print(fib_generate(3))
# print(fib_generate(4))
# print(fib_generate(5))
# print(fib_ge(0))
# print(fib_ge(1))
# print(fib_ge(2))
# print(fib_ge(3))
# print(fib_ge(4))
# print(fib_ge(5))

@log_execution_time
def test_fib_ge():
    print('测试迭代版递归函数：')
    fib_generate(60)

print('*'*80)
test_fib_ge()







