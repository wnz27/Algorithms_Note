'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-23 23:06:05
@LastEditTime: 2020-02-23 23:06:05
@FilePath: /Algorithms_Note/pat相关/乙级/2.py
@description: type some description
'''
'''
读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：
每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10的100次方
输出格式：
在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

输入样例：
1234567890987654321123456789
输出样例：
yi san wu
'''
n = str(input())
sum = 0
pinyin = ' '
pinying_dict = {'1': 'yi', '2':'er', '3': 'san', '4':'si', '5':'wu', 
                '6':'liu', '7': 'qi', '8':'ba', '9':'jiu', '0': 'ling'}
for char in n:
    sum += int(char)
for char in str(sum):
    pinyin += (pinying_dict[char] + ' ')
print(pinyin.strip())