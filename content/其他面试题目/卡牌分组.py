'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-27 08:47:09
@LastEditTime: 2020-03-27 09:22:52
@FilePath: /Algorithms_Note/content/其他面试题目/卡牌分组.py
@description: type some description
'''
'''
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：
输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：
输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：
输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]
提示：
1 <= deck.length <= 10000
0 <= deck[i] < 10000
'''
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from fractions import gcd
        import collections
        helper = collections.Counter(deck).values()
        return reduce(gcd, helper) >= 2