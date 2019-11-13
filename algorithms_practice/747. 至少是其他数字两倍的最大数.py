class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, value in enumerate(nums):
            if index == nums.index(max(nums)):
                continue
            elif max(nums) >= 2*value:
                continue
            else:
                return -1
        return nums.index(max(nums))