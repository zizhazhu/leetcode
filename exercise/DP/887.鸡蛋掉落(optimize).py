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
                low, high = 2, j
                while low < high:
                    middle = (low + high) // 2
                    broken = times[i-1][middle-1]
                    perfect = times[i][j-middle]
                    if broken > perfect:
                        times[i][j] = min(times[i][j], broken + 1)
                        high = middle
                    else:
                        times[i][j] = min(times[i][j], perfect + 1)
                        low = middle + 1
        return times[K][N]
# @lc code=end

