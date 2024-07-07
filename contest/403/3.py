from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        positive, negative = nums[0], -1000000001
        for i in range(1, len(nums)):
            next_positive = max(positive, negative) + nums[i]
            negative = positive - nums[i]
            positive = next_positive
        return max(positive, negative)


solution = Solution()
print(solution.maximumTotalCost([1, -2, 3, 4]))  # 5