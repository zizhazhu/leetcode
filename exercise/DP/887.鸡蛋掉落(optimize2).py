#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        times = [[0 for i in range(0, N + 1)] for j in range(0, K + 1)]
        for i in range(1, K + 1):
            j = 1
            while True:
                times[i][j] = times[i-1][j-1] + times[i][j-1] + 1
                if times[i][j] >= N:
                    if i == K:
                        return j
                    break
                j += 1
# @lc code=end

