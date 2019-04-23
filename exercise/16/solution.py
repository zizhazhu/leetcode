class Solution:
    def threeSumClosest(self, nums: list[int], target: int)->int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if abs(temp - target) < abs(closest - target):
                    closest = temp

