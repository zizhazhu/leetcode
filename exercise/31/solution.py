class Solution:
    def reverseNums(self, nums: List[int], left: int, right: int):
        end = left + (right - left) // 2
        for i in range(left, end):
            nums[i], nums[right-i-1] = nums[right-i-1], nums[i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        now = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                now = i
                break
        next_num = now + 1
        if now > 0:
            for i in range(now + 1, len(nums)):
                if nums[i] < nums[now]:
                    next_num = i - 1
            nums[now], nums[next_num] = nums[next_num], nums[now]
        self.reverseNums(nums, now + 1, len(nums))
