#! -*- coding=utf-8 -*-
'''
快速排序三步走
1、Partition：选择基准分割数组为两个子数组，小于基准和大于基准
2、对两个子数组进行快速排序
3、合并结果

代码实现分析
1、递归出口，退出条件，当数组长度小于2的时候直接返回数组
2、选择基准，遍历找出小于和大于基准的数组
3、合并结果

总结：其实可以看出代码基本就是翻译工作
'''
def quicksort(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        pivot_index = 0  # 把第一个索引的数当做基准
        pivot = array[pivot_index]
        less_part = [
            i for i in array[pivot_index+1:] if i <= pivot
        ]
        great_part = [
            i for i in array[pivot_index+1:] if i > pivot
        ]
        return quicksort(less_part) + [pivot] + quicksort(great_part)

# 测试快速排序
def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(quicksort(ll))
    print(sorted(ll))
    assert quicksort(ll) == sorted(ll)

test_quicksort()
