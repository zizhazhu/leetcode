class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sort(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                while left < right - 1 and nums[left] == nums[left+1]:
                    left += 1
                while left < right - 1 and nums[right] == nums[right-1]:
                    right -= 1
                now = nums[i] + nums[left] + nums[right]
                if now == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif now < 0:
                    left += 1
                else:
                    right -= 1
        return result

