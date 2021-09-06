#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        not_same = []
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue
            else:
                not_same.append(i)
        if len(not_same) == 0:
            alpha_set = set()
            for i in range(len(s)):
                if s[i] in alpha_set:
                    return True
                else:
                    alpha_set.add(s[i])
            return False
        elif len(not_same) == 2 and s[not_same[0]] == goal[not_same[1]] and s[not_same[1]] == goal[not_same[0]]:
            return True
        else:
            return False

# @lc code=end

