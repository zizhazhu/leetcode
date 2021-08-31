#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now = -1
        result = 0
        for i in range(len(prices)):
            if i == len(prices) - 1 or prices[i+1] <= prices[i]:
                if now == -1:
                    continue
                else:
                    result += prices[i] - now
                    now = -1
            else:
                if now == -1:
                    now = prices[i]
        return result
# @lc code=end

