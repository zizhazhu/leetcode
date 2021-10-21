#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        result = 0
        for num in nums:
            if num - 1 in exists:
                continue
            else:
                last = num
                while last in exists:
                    if result < last - num + 1:
                        result = last - num + 1
                    last += 1
        return result

# @lc code=end

