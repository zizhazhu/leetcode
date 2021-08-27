#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        f = [n for i in range(n + 1)]
        f[0] = 0
        for i in range(n):
            j = 1
            next_value = i + j * j
            while next_value <= n:
                if f[next_value] > f[i] + 1:
                    f[next_value] = f[i] + 1
                j += 1
                next_value = i + j * j
        return f[n]
# @lc code=end

