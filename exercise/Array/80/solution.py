class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        pre = 1
        for i in range(2, len(nums)):
            if nums[pre] == nums[pre-1] and nums[i] == nums[pre]:
                continue
            pre += 1
            nums[pre] = nums[i]
        return pre + 1
