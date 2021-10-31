class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sum_until = list(nums)
        result = sum_until[0]
        for i in range(1, len(nums)):
            if sum_until[i-1] + nums[i] > sum_until[i]:
                sum_until[i] = sum_until[i-1] + nums[i]
            if result < sum_until[i]:
                result = sum_until[i]
        return result
