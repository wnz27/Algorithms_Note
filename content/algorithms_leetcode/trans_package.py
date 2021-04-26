# -*- coding:utf-8 -*-
# @UpdateTime : 2021/4/26 5:58 下午
# @Author : a27
"""
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
"""
from typing import List


# 最小运载就是货物里的最大值，每天都能搬走一个， 最大运载力就是一天运完即货物的重量和
# 在这之间找到一个最小的运载力，可以在 D 天运完
class Solution:

    def count_days(self, trans_cap, weights: List[int]) -> int:
        """ 获取运载能力为trans_cap时需要的天数 """
        days = 1
        current_w = 0
        for w in weights:
            current_w += w
            if current_w > trans_cap:
                days += 1
                current_w = w
        return days

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_cap = max(weights)

        max_cap = sum(weights)

        target = D

        while min_cap < max_cap:
            mid_cap = (max_cap + min_cap) // 2
            count_days = self.count_days(mid_cap, weights)

            if count_days > target:  # 运载能力不够
                min_cap = mid_cap + 1
            else:
                max_cap = mid_cap
        return min_cap


if __name__ == '__main__':
    s = Solution()
    # a = s.count_days(10, [1,2,3,4,5,6,7,8,9,10])
    # print(a)
    pass