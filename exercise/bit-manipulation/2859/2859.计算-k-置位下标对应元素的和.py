#
# @lc app=leetcode.cn id=2859 lang=python
#
# [2859] 计算 K 置位下标对应元素的和
#

# @lc code=start
class Solution(object):
    def countBin(self, num):
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num >>= 1
        return count

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

