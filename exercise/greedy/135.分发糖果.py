#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0 for _ in range(len(ratings))]
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            else:
                candies[i] = 1
        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings) - 1 and ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
            else:
                candies[i] = max(1, candies[i])
        return sum(candies)
            
# @lc code=end

