#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums.sort()
        num_list = []
        def dfs(index):
            if index == len(nums):
                results.add(tuple(num_list))
            else:
                dfs(index+1)
                num_list.append(nums[index])
                dfs(index+1)
                num_list.pop()
        dfs(0)

        return list(results)
# @lc code=end

