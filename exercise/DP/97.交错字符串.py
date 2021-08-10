#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        f = [[False for _ in range(len(s1) + 1)] for _ in range(len(s3) + 1)]
        f[0][0] = True
        for i in range(len(s3)):
            for j in range(max(0, i - len(s2)), min(len(s1) + 1, i + 1)):
                if f[i][j]:
                    if j < len(s1) and s3[i] == s1[j]:
                        f[i+1][j+1] = True
                    if i - j < len(s2) and s3[i] == s2[i-j]:
                        f[i+1][j] = True
        return f[len(s3)][len(s1)]
                
# @lc code=end

s = Solution()
s.isInterleave("aabcc", "dbbca", "aadbbcbcac")

