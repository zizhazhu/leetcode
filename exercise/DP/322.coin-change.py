#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coin_cnt = [-1 for i in range(amount + 1)]
        coin_cnt[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                prev = i - coin
                if prev < 0 or coin_cnt[prev] == -1:
                    continue
                if coin_cnt[i] == -1 or coin_cnt[i] > coin_cnt[prev] + 1:
                    coin_cnt[i] = coin_cnt[prev] + 1
        return coin_cnt[amount]
        
# @lc code=end

