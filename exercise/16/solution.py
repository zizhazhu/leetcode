class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if abs(temp - target) < abs(closest - target):
                    closest = temp
                if temp - target < 0:
                    left += 1
                elif temp - target > 0:
                    right -= 1
                else:
                    return temp
        return closest

