#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def __init__(self):
        self.root = {}

    def rooted(self, a):
        if self.root[a] != a:
            self.root[a] = self.rooted(self.root[a])
        return self.root[a]

    def merge(self, a, b):
        if a < b:
            self.root[b] = self.rooted(a)
        else:
            self.root[a] = self.rooted(b)

    def same(self, a, b):
        return self.rooted(a) == self.rooted(b)

    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
            self.root[num] = num
        for num in nums:
            if num - 1 in exists:
                self.merge(num - 1, num)
        result = 0
        for num in nums:
            root = self.rooted(num)
            if result < num - root + 1:
                result = num - root + 1
        return result
# @lc code=end

