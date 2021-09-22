class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one, two = 0, 0
        for now in range(len(nums)):
            if nums[now] == 0:
                nums[two], nums[now] = nums[now], nums[two]
                nums[two], nums[one] = nums[one], nums[two]
                one += 1
                two += 1
            elif nums[now] == 1:
                nums[two], nums[now] = nums[now], nums[two]
                two += 1
            else:
                pass

