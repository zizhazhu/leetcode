#
# @lc app=leetcode.cn id=2859 lang=python
#
# [2859] 计算 K 置位下标对应元素的和
#

# @lc code=start
class Solution(object):
    def countBin(self, num):
        result = ((num & 0b1010101010) >> 1) + (num & 0b0101010101)
        result = ((result & 0b0011001100) >> 2) + (result & 0b1100110011)
        result = (result >> 8) + ((result >> 4) & 0b1111) + (result & 0b1111)
        return result

    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            if self.countBin(i) == k:
                result += nums[i]
        return result
# @lc code=end

