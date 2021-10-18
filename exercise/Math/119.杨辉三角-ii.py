#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(1, rowIndex + 1):
            last = result[-1]
            result.append(last * (rowIndex - i + 1) // i)
        
        return result

# @lc code=end

