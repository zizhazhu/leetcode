class Solution:
    def quick(self, nums: List[int], k: int, begin: int, end: int) -> int:
        mid = nums[end]
        left = begin
        for i in range(begin, end):
            if nums[i] > end:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        nums[end], nums[left] = nums[left], nums[mid]
        if left == k:
            return nums[left]
        elif left < k:
            quick(nums, k, left + 1, end)
        else:
            quick(nums, k , begin, left - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick(nums, k - 1, 0, len(nums) - 1)

