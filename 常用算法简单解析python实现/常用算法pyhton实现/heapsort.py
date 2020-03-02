#! -*- coding=utf-8 -*-
'''
利用python现有的堆库
先把无序的要排序的可迭代对象的每个元素压入堆，
然后再pop出来，heappop每次推出最小的数，并且还保持堆结构
'''
from heapq import heappush, heappop

def heapqsort(iterable):
    res = []
    for item in iterable:
        heappush(res, item)
    return [heappop(res) for i in range(len(res))]

def test_heapsort():
    import random
    ll = list(range(20))
    random.shuffle(ll)
    print(ll)
    assert sorted(ll) == heapqsort(ll)
    print(heapqsort(ll))

test_heapsort()