'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-24 10:04:29
@LastEditTime: 2020-03-24 10:46:42
@FilePath: /Algorithms_Note/content/其他面试题目/按摩师.py
@description: type some description
'''
'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
注意：本题相对原题稍作改动
示例 1：
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：
输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：
输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
'''
class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d_i_2 = 0   # 两天前最大值
        d_i_1 = 0   # 一天前最大值
        for time in nums:
            d_curr = max(d_i_2 + time, d_i_1)   # 当天最大值
            d_i_2, d_i_1 = d_i_1, d_curr        # 进入下一天前，把当天给一天前最大值，一天前最大值的给两天前最大值
        return d_i_1