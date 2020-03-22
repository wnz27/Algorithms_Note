'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-08 09:04:17
@LastEditTime: 2020-03-08 19:06:28
@FilePath: /Algorithms_Note/algorithms_leetcode/零钱兑换.py
@description: type some description
'''
'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
'''
# 方法一，自上而下
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = coins
        self.res = {}
        if amount < 1:
            return 0
        else:
            return self.dp(amount)

    def dp(self, amount):
        if amount < 0: return -1
        if amount == 0: return 0
        if amount in self.res:
            return self.res[amount]
        mini = int(1e9)
        for coin in self.coins:
            tem = self.dp(amount - coin)
            if tem >= 0 and tem < mini:
                mini = tem + 1
        if mini < int(1e9):
            self.res[amount] = mini
            return mini
        else:
            # 当这个数不能被这些coin凑成则，也记录这个数，方便其他使用，不写为啥会卡住？？？
            self.res[amount] = -1
            return -1
# s = Solution1()
# print(s.coinChange([186,419,83,408],6249))
# print(s.res)

# 方法二、自下而上
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
s = Solution()
print(s.coinChange([186,419,83,408],6249))


'''
[2,5,10,1],27
[186,419,83,408],6249
'''
