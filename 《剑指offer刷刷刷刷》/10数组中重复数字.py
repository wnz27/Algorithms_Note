'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-10 07:26:11
@LastEditTime: 2020-03-10 08:55:22
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/数组中重复数字.py
@description: type some description
'''
'''
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
'''
class Solution(object):
    # 方法一，哈希,好处是可以记录所有重复的，缺点代码稍多
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = {}
        res = []
        # 哈希
        for i in nums:
            if i in helper:
                helper[i] += 1
            helper.setdefault(i, 1)
        for k,v in helper.items():
            if v > 1:
                res.append(k)
        if res != []:
            random.shuffle(res)
            return res[0]
        else:
            return -1
    # 方法二，集合，好处是实现简单，缺点是重复的数字只会捕捉遇见的第一个，找不齐。
    def findRepeatNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = set({})
        for i in nums:
            if i in helper:
                return i
            else:
                helper.add(i)
        return -1
s = Solution()
print(s.findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))
