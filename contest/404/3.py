from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0] * k for _ in range(k)] 
        result = 0
        for i, num in enumerate(nums):
            delta = num % k
            for target in range(k):
                last = (target - delta + k) % k
                f[target][delta] = max(f[target][delta], f[target][last] + 1)
                result = max(result, f[target][delta])
        return result


solution  = Solution()
print(solution.maximumLength([1, 2, 3, 4, 5], 2))  # 5

