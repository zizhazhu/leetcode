#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        acc_nums = [0]
        for i in range(len(nums)):
            acc_nums.append(acc_nums[-1] + nums[i])
        if acc_nums[-1] < target:
            return 0
        length = len(nums)

        def search(left, right):
            # [left, right)
            edge = left
            while left < right:
                mid = (left + right) // 2
                sum_p = acc_nums[mid] - acc_nums[edge]
                if sum_p == target:
                    return mid
                elif sum_p > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        min_len = length
        for i in range(len(nums)):
            right = search(i, length)
            if acc_nums[right] - acc_nums[i] >= target:
                min_len = min(min_len, right - i)
        return min_len
# @lc code=end
s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

