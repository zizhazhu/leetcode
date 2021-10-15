#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            next_row = [1]
            for j in range(1, i):
                next_row.append(result[i-1][j-1] + result[i-1][j])
            next_row.append(1)
            result.append(next_row)
        return result
# @lc code=end

