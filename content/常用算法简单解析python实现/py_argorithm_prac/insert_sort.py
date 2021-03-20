# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/20 4:51 下午
# @Author : a27
# @Description: 插入排序
from typing import List


def insert_sort(arr: List[int]):
    for i in range(len(arr)):
        j = i
        while j - 1 >= 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
            j -= 1
        print("for:{}:".format(i + 1), arr)
    return arr


if __name__ == '__main__':
    a = [1, 2, -30, 399, 46, -3454, -40, 200]
    s_a = insert_sort(a)
    print(s_a)
    pass
