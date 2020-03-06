'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-29 16:43:25
@LastEditTime: 2020-02-29 18:06:20
@FilePath: /Algorithms_Note/algorithms_practice/MaxConsecutiveOnes.py
@description: type some description
'''
'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution:
    # 方法一，分段计数，返回最大段的值，无法记录最大段的起始位置
    def findMaxConsecutiveOnes(self, nums):
        if len(nums) < 1:
            return -1
        res = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res.append(count)
                count = 0
        res.append(count)
        return max(res)
    # 方法二，快慢指针，可以保留位置信息的方法
    def findMaxConsecutiveOnes2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return -1
        if n == 1:
            if nums[0] == 1:
                return 1
            else:
                return 0
        slow = 0
        fast = 1
        res=[]
        while fast < n:
            if nums[fast] == 0:
                if nums[fast - 1] == 1:
                    res.append((slow,fast))  # 连续1的始末位置，左闭右开
                slow = fast
                if fast == n-1:  #  防止最后连续0的情况出现多计数的情形
                    break
            else:
                if nums[fast - 1] == 0:
                    slow = fast
            fast += 1
        res.append((slow, fast))  # 防止最后都是1的情形
        res = max(res, key=lambda x: x[1] - x[0])
        return res[1] - res[0]
s = Solution()
b = s.findMaxConsecutiveOnes2([0,0])
print(b)

