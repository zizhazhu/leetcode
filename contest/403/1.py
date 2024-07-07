class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_float = 100000.0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            avg = (nums[i] + nums[j]) / 2
            min_float = min(min_float, avg)
            i += 1
            j -= 1
        return min_float