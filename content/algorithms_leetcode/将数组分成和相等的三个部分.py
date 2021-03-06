'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 00:10:14
@LastEditTime: 2020-03-11 00:47:46
@FilePath: /Algorithms_Note/algorithms_leetcode/将数组分成和相等的三个部分.py
@description: type some description
'''
'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] ==
 A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false

示例 3：
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
'''
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        num = sum(A)
        if num % 3 != 0:
            return False
        count = cnt = 0  #  cnt累加器，看看有几次归零操作,几次可以是和的三分之一，至少超过三次，才可以做3等分，针对零的情况
        for i in A:
            count += i
            if count == num / 3:
                count = 0
                cnt += 1
        return count == 0 and cnt == 3