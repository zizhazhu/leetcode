#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
        return sum(len(word) + 1 for word in words_set)

# @lc code=end

