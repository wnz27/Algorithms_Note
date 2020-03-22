'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 12:10:18
@LastEditTime: 2020-03-14 12:30:00
@FilePath: /Algorithms_Note/其他面试题目/打乱数组.py
@description: type some description
'''
'''
打乱一个没有重复元素的数组。
示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);
// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();
// 重设数组到它的初始状态[1,2,3]。
solution.reset();
// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
'''
# deep copy
class Solution1(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__data = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__data

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import copy
        n = len(self.__data)
        tem_data = copy.deepcopy(self.__data)
        import random
        for i in range(n):
            tem = random.randint(i, n-1)
            tem_data[i], tem_data[tem] = tem_data[tem], tem_data[i]
        return tem_data

# 增加originlist
class Solution(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__data = nums
        self.__original = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.__data = self.__original
        self.__original = list(self.__original)
        return self.__data
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        n = len(self.__data)
        for i in range(n):
            tem = random.randint(i, n-1)
            self.__data[i], self.__data[tem] = self.__data[tem], self.__data[i]
        return self.__data


s = Solution([1,2,3])
print(s.shuffle())
print(s.reset())