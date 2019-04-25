class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[len(nums)-1] + nums[len(nums)-2] < target:
                    continue
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    now = nums[i] + nums[j] + nums[left] + nums[right]
                    if now < target:
                        left += 1
                    elif now > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return result
