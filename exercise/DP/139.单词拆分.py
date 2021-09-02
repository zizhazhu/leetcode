#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        valid = [False for _ in range(len(s)+1)]
        def isBreak(start):
            for word in wordDict:
                if len(word) > length - start:
                    continue
                flag = True
                for i in range(len(word)):
                    if s[start + i] != word[i]:
                        flag = False
                        break
                if flag:
                    valid[start + len(word)] = True
        valid[0] = True
        for i in range(len(s)):
            if valid[i]:
                isBreak(i)
        return valid[len(s)]

# @lc code=end

