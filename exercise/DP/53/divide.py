class Solution:
    def maxSubArrayPart(self, nums, left, right):
        if left == right:
            return nums[left], nums[left], nums[left], nums[left]
        mid = (left + right) // 2
        left_left, left_max, left_right, left_sum = self.maxSubArrayPart(nums, left, mid)
        right_left, right_max, right_right, right_sum = self.maxSubArrayPart(nums, mid + 1, right)
        all_left = max(left_left, left_sum + right_left)
        all_right = max(right_right, right_sum + left_right)
        all_max = max(left_max, right_max, left_right + right_left)
        all_sum = left_sum + right_sum
        return all_left, all_max, all_right, all_sum

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        _, result, _, _ = self.maxSubArrayPart(nums, 0, len(nums) - 1)
        return result
