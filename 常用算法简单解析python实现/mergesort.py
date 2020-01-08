#! -*- coding=utf-8 -*-
'''
合并两个有序数组
先找一个空数组来接收最后结果
设想两个指针分别指向两个数组的第一位，开始比较
哪个小就把这个数添加到结果数组中，并把这个数组上的指针前进一位
以此类推。
代码实现：
结果数组，两个指针
指针前进条件：当下指针位置不是最后一位
如果一个数组的指针已经等于数组长度，那么就直接把另一个数组从指针位置到数组末尾的数加进结果数组
'''
def merge_sorted_list(array1, array2):
    result_array = []  # 存放结果的数组
    index1 = 0  # 标识第一个数组的指针
    index2 = 0  # 标识第二个数组的指针
    while True:
        if (index1 == len(array1)) & (index2 == len(array2)):
            break
        elif (index1 == len(array1)) & (index2 < len(array2)):
            for i in array2[index2:]:
                result_array.append(i)
            index2 = len(array2)
            continue
        elif (index1 < len(array1)) & (index2 == len(array2)):
            for i in array1[index1:]:
                result_array.append(i)
            index1 = len(array1)
            continue
        else:
            if array1[index1] <= array2[index2]:
                result_array.append(array1[index1])
                index1 += 1
                continue
            else:
                result_array.append(array2[index2])
                index2 += 1
                continue
    return result_array
        
# 仔细再考虑上面的【合并】代码可以再做优化
def optimize_merge_sorted_array(sortedArray1, sortedArray2):
    length_1, length_2 = len(sortedArray1), len(sortedArray2)
    index1 = index2 = 0
    merge_result_array = []
    while index1 < length_1 and index2 < length_2:
        if sortedArray1[index1] <= sortedArray2[index2]:
            merge_result_array.append(sortedArray1[index1])
            index1 += 1
        else:
            merge_result_array.append(sortedArray2[index2])
            index2 += 1
    if index1 < length_1:
        merge_result_array.extend(sortedArray1[index1:])
    else:
        merge_result_array.extend(sortedArray2[index2:])
    return merge_result_array

def test_mergearray():
    import random
    array1 = list(range(10))
    print(array1)
    array2 = list(range(5,20))
    print(array2)
    print(merge_sorted_list(array1, array2))

def test_mergearray_optimize():
    import random
    array1 = list(range(10))
    print(array1)
    array2 = list(range(5,20))
    print(array2)
    print(optimize_merge_sorted_array(array1, array2))

test_mergearray()
print('*' * 80)
test_mergearray_optimize()

'''
写完合并之后就可以考虑归并排序了
如何使用上面的合并来排序？
这样想，如果两个数组都只有一个数，那么我用合并之后他们是什么情况？
没错，肯定是排好序的两个元素的数组。
为了利用合并排好序的数组来排无序的整个数组，那我们肯定要把这个数组分割为很多个只有一个元素的数组
然后依次合并最终形成有序的数组
所以我们思考代码：
递归出口肯定是只有一个元素的数组直接返回
否则，我们把数组从中间分割为两个部分，对每个部分分别排序
最后对两个排好序的部分进行合并。
'''
def merge_sort(array):
    if len(array) < 2:  # 有一个元素是递归出口
        return array
    else:
        middle = int(len(array)/2)
        left_array = merge_sort(array[:middle])
        right_array = merge_sort(array[middle:])
        # 合并有序数组
        return optimize_merge_sorted_array(left_array, right_array)

# 再做一下测试
def test_merge_sort():
    import random
    ll = list(range(30))
    random.shuffle(ll)
    print(ll)
    print(merge_sort(ll))
    assert merge_sort(ll) == sorted(ll)

test_merge_sort()
