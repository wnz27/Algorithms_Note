'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 10:15:57
@LastEditTime: 2020-03-12 10:26:09
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/14数据流中的中位数.py
@description: type some description
'''
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后
位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

限制：
最多会对 addNum、findMedia进行 50000 次调用。
'''
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []


    def addNum(self, num):
        lo, hi = 0, len(self.__data)
        tem_index = self.__binary_search_for_insert_index(lo,hi,num)
        self.__data.insert(tem_index, num)
    
    # 借助二分法用收紧右边界，找左边界方法插入数据使数组有序，logn, 
    # 找不到的情况也能拿到大于目标值的最靠前的一个数的索引
    def __binary_search_for_insert_index(self, lo, hi, target):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.__data[mid] == target:
                hi = mid
            elif target < self.__data[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def findMedian(self):
        if self.size % 2 == 0:  # 偶数情况
            return self.__data[self.size // 2 - 1] / 2 + self.__data[self.size // 2] / 2
        else:                   # 奇数情况
            return self.__data[self.size // 2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()