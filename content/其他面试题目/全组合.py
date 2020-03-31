'''
@Author: 27
@LastEditors: 27
@Date: 2020-04-01 01:13:01
@LastEditTime: 2020-04-01 01:13:34
@FilePath: /Algorithms_Note/content/其他面试题目/全组合.py
@description: type some description
'''
# 字符串的解决方案
def co_k1(lst, k):
    if k == 0:
        return [""]
    helper = []
    for i in range(len(lst)):
        for sub in co_k1(lst[i+1:], k-1):
            helper += [lst[i] + sub]
    return helper
def co_all1(lst):
    res = []
    for i in range(1, len(lst)+1):
        res += co_k1(lst, i)
    return res

a = co_all1("abc")
print(a)
# 数组的解决方案
class Solution:
    def co_k(self, lst, k):
        n = len(lst)
        def backtrack(first = 0, curr = []):
            # 如果长度达标把结果装起来
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add i into the current combination
                curr.append(lst[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        output = []
        backtrack()
        return output
        
    def co_all(self, lst):
        res = []
        for i in range(1, len(lst)+1):
            tmp = self.co_k(lst, i)
            res.extend(tmp)
        return res
s = Solution()
b = s.co_all([1,2,3,4])
print(b)
