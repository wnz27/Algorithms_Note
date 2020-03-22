'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-20 00:33:51
@LastEditTime: 2020-03-20 00:34:27
@FilePath: /Algorithms_Note/其他面试题目/最小的k个数.py
@description: type some description
'''
'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，
输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = sorted(arr)
        return a[:k]