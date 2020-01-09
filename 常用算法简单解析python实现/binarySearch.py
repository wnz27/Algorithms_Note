#! -*- coding=utf-8 -*-
'''
二分查找也要需要会手写，注意边界；python有个内置的bisect模块
两种实现,
1、普通方式：
记录起始的索引，末尾的索引
找到中间索引的值与目标值比较，
如果比目标值大那么说明目标值在数组的前半部分，那么就把末尾的索引变成这个中间索引-1，重复找中间索引值的操作
如果比目标值小那么说明目标值在数组的后半部分，那么就把起始的索引变成这个中间索引+1，重复找中间索引值的操作
2、递归方式
递归出口是要么查找的目标数组为空或者起始索引大于结束索引
返回结果依旧是如果中间索引的值是目标值则返回
如果目标值大于中间索引的值那么就在后半部分，对后半部分（mid_index + 1 到 end_index）递归查找
如果目标值小于中间索引的值那么就在前半部分，对前半部分（begin_index 到 mid_index - 1）递归查找
'''
def biSearchNormal(sorted_array, target_value):
    if not sorted_array:
        return -1
    begin_index = 0
    end_index = len(sorted_array) - 1
    while begin_index <= end_index:
        mid_index = int((begin_index + end_index) / 2)
        if target_value == sorted_array[mid_index]:
            return mid_index
        elif target_value > sorted_array[mid_index]:
            begin_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return -1

def biSearchRecursion(sorted_array, begin_index, end_index, target_value):
    if not sorted_array or begin_index > end_index:
        return -1
    mid_index = int((begin_index + end_index)/2)
    if sorted_array[mid_index] == target_value:
        return mid_index
    elif sorted_array[mid_index] > target_value:
        return biSearchRecursion(sorted_array, begin_index, mid_index - 1, target_value)
    else:
        return biSearchRecursion(sorted_array, mid_index + 1, end_index, target_value)

def test_biSearch():
    l = range(10)
    assert biSearchRecursion(l, 0, len(l)-1, 7) == biSearchNormal(l, 7)

test_biSearch()
    
