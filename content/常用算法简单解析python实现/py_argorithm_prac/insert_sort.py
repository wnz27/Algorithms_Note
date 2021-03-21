# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/20 4:51 下午
# @Author : a27
# @Description: 插入排序
from typing import List
"""
插入排序的特性：
重要特性，对于有序数组，插入排序的复杂度是On的，与选择排序对比来说选择排序永远是On方的。
但是整体来看插入排序的复杂度依然是On方的。

如果业务上大多是有序的数据结构，用插入排序也是比较好的选择。
"""

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


def insert_sort_update(arr: List[int]):
    for i in range(len(arr)):
        j = i
        curr_value = arr[i]
        while j - 1 >= 0:
            if curr_value < arr[j - 1]:  # 如果这个值小于前一位
                arr[j] = arr[j - 1]  # 前一位往后移动
            else:
                arr[j] = curr_value
                break  # 不跳出赋值会出问题，前面都给盖掉了
            j -= 1
    return arr


def insert_sort_update2(arr: List[int]):
    for i in range(len(arr)):
        j = i
        curr_value = arr[i]
        while (j - 1 >= 0) and (curr_value < arr[j - 1]):
            arr[j] = arr[j - 1]  # 前一位往后移动
            j -= 1
        arr[j] = curr_value
    return arr


if __name__ == '__main__':
    a = [1, 2, -30, 399, 46, -3454, -40, 200]
    s_a = insert_sort(a)
    print(s_a)
    s_a_up = insert_sort_update(a)
    print(s_a_up)
    s_a_up2 = insert_sort_update2(a)
    print(s_a_up2)
    pass
