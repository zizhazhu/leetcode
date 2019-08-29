class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid]:
                left += 1
            elif nums[mid] == nums[right]:
                right -= 1
            elif target < num[mid]:
                if target >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
                    
