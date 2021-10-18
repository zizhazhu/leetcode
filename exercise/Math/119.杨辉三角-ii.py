#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        def fact(begin, n):
            result = 1
            for i in range(n):
                result *= begin
                begin -= 1
            return result

        for i in range(1, rowIndex // 2 + 1):
            num = fact(rowIndex, i) // fact(i, i)
            result.append(num)

        for i in range((rowIndex - 1) // 2, -1, -1):
            result.append(result[i])
        
        return result

# @lc code=end

