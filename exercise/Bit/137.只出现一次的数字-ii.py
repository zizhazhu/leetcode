#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        upper, lower = 0, 0
        # 0 -> 1 -> 10 -> 0
        for num in nums:
            has_upper = upper & num
            upper -= has_upper
            other = num - has_upper
            has_lower = other & lower
            upper |= has_lower
            lower ^= other
        
        return lower

# @lc code=end

