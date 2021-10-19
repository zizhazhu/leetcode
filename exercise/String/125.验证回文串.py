#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s_list = []
        for c in s:
            if '0' <= c <= '9':
                new_s_list.append(c)
            elif 'a' <= c <= 'z':
                new_s_list.append(c)
            elif 'A' <= c <= 'Z':
                new_s_list.append(str.lower(c))
        for i in range(len(new_s_list) // 2):
            if new_s_list[i] != new_s_list[-i-1]:
                return False
        return True
# @lc code=end

