class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            num = nums[mid]
            if num == target:
                return mid
            if num >= nums[left]:
                if num < target:
                    left = mid + 1
                else:
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if num > target:
                    right = mid - 1
                else:
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1

