from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even = 0, 0
        same_odd, same_even = 0, 0
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even = max(even, odd + 1)
                same_even += 1
            else:
                odd = max(odd, even + 1)
                same_odd += 1
        return max(odd, even)
            
