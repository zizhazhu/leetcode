class Solution:
    def climbStairs(self, n: int) -> int:
        before_2, before = 1, 1
        for i in range(1, n):
            now = before_2 + before
            before_2, before = before, now
        return before
