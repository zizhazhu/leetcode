#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        length = 1 << n
        reflect = 0
        change = 0
        for i in range(1, length):
            if (i - 1) & i == 0:
                reflect = i - 1
                change = i
            num = result[reflect] | change
            reflect -= 1
            result.append(num)
                
        return result
# @lc code=end

