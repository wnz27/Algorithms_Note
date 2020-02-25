'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-23 23:06:57
@LastEditTime: 2020-02-24 10:52:52
@FilePath: /Algorithms_Note/pat相关/乙级--python/4.py
@description: type some description
'''

'''
读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

输入格式：
每个测试输入包含 1 个测试用例，格式为
第 1 行：正整数 n
第 2 行：第 1 个学生的姓名 学号 成绩
第 3 行：第 2 个学生的姓名 学号 成绩
  ... ... ...
第 n+1 行：第 n 个学生的姓名 学号 成绩
其中姓名和学号均为不超过 10 个字符的字符串，成绩为 0 到 100 之间的一个整数，
这里保证在一组测试用例中没有两个学生的成绩是相同的。

输出格式：
对每个测试用例输出 2 行，第 1 行是成绩最高学生的姓名和学号，
第 2 行是成绩最低学生的姓名和学号，字符串间有 1 空格。

输入样例：
3
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95

输出样例：
Mike CS991301
Joe Math990112
'''

n = int(input())

result = {}
mini = 101
maxi = -1
for _ in range(n):
    inp = input()
    g = inp.split()
    g[2] = int(g[2])
    if g[2] > maxi:
        maxi = g[2]
        result['max'] = g
    if g[2] < mini:
        mini = g[2]
        result['min'] = g

print(result["max"][0], result["max"][1])
print(result["min"][0], result["min"][1])

    
# 通过

a = int(input())
 
maxi = -1
mini = 101
 
for i in range(0, a):
    line = input()
    cmp = line.split()
    if int(cmp[2]) > maxi:
        c = line
        maxi = int(cmp[2])
    if int(cmp[2]) < mini:
        d = line
        mini = int(cmp[2])
 
c = c.split()
d = d.split()
 
print(c[0] + " " + c[1])
print(d[0] + " " + d[1])
