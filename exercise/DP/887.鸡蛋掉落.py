#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        times = [[0 for i in range(0, N + 1)] for j in range(0, K + 1)]
        for i in range(0, N + 1):
            times[1][i] = i
        for i in range(2, K + 1):
            times[i][1] = 1
            for j in range(2, N + 1):
                times[i][j] = times[i][j-1] + 1
                for k in range(2, N):
                    times[i][j] = min(times[i][j],
                                      max(times[i-1][k-1], times[i][j - k]) + 1)
        return times[K][N]
# @lc code=end

