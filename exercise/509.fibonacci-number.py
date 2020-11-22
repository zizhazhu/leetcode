#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            pre_prev, prev = 0, 1
            for i in range(N - 1):
                result = pre_prev + prev
                pre_prev, prev = prev, result
            return result
        
# @lc code=end

