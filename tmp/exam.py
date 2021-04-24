# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/4/24 10:57
# @Author    : 27
# @File    : exam.py
"""
二维矩阵 最大值
"""
import sys
from typing import List, Tuple


def move_right_list(values: List[str]) -> List[str]:
    # 我其实就是要找到移动完起始位置是谁，比如移动一位，则现在的最后一个元素是起始位置
    # 迁移到一般就是找到n个位置，但是这里面要有取余考虑
    return values[-1] + values[:-1]


def count_1(values: List[str]) -> int:
    count = 0
    for v in values:
        if v == "1":
            count += 1
    return count


def get_middle_idx(values: List[str]) -> Tuple[int, bool]:
    # 并 告知是双数还是单数
    is_odd = False
    if len(values) % 2 != 0:
        is_odd = True
    return int(len(values) / 2), is_odd


def get_two_side_count1(values: List[str]) -> Tuple[int, int]:
    middle_idx, is_odd = get_middle_idx(values)
    print(values)
    if is_odd:
        return count_1(values[:middle_idx]), count_1(values[middle_idx+1:])
    else:
        return count_1(values[:middle_idx + 1], count_1(values[middle_idx + 1:]))


def values2max_binary_seq(values: List[str]) -> List[str]:
    # 【核心逻辑】 把列表进行右移左移找到最大的那个顺序
    # 遍历一遍试的话会让整个算法变成n^2
    # 左右移动的话尝试试一半也可以达到效果会降低复杂度 但是量级并没有减少
    # 题目的N 不大于20 那么就暴力解决吧。。。。
    # 保证第一位是1的前提下，左半边的1 的个数 大于右半边 且右边结束不是1就行了。 是不是有点儿讨巧。。。
    left_1_value, right_1_value = get_two_side_count1(values)
    if not left_1_value and not right_1_value:
        return values
    while values[0] != "1" or left_1_value < right_1_value or values[-1] == "1":
        values = move_right_list(values)
        left_1_value, right_1_value = get_two_side_count1(values)
    return values


def values_of_max_base10(values_of_max_seq_line: List[str]) -> int:
    # 1、列表里面所有元素拼接为二进制串
    binary_string = "".join(values_of_max_seq_line.split(","))
    # 2、变为十进制数
    max_value = int(binary_string, base=2)
    return max_value


def max_matrix():
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        line = sys.stdin.readline().strip()
        max_seq_line = values2max_binary_seq(line)
        print(max_seq_line)
        max_value = values_of_max_base10(max_seq_line)
        ans += max_value
    print(ans)


if __name__ == '__main__':
    # 主体逻辑

    max_matrix()

    pass
