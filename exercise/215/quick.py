class Solution:
    def quick(self, nums: List[int], k: int, begin: int, end: int) -> int:
        mid = nums[end]
        left = begin
        for i in range(begin, end):
            if nums[i] > mid:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        nums[end], nums[left] = nums[left], nums[end]
        if left == k:
            return nums[left]
        elif left < k:
            self.quick(nums, k, left + 1, end)
        else:
            self.quick(nums, k , begin, left - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick(nums, k - 1, 0, len(nums) - 1)

