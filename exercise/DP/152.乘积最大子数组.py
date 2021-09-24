#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = nums[0]
        min_product = 1
        max_product = 1
        for num in nums:
            new_min_product = min(min_product * num, max_product * num, num)
            new_max_product = max(min_product * num, max_product * num, num)
            min_product = new_min_product
            max_product = new_max_product
            if result < max_product:
                result = max_product
        return result
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))