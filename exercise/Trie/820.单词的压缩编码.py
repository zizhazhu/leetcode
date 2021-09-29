#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        nodes = []
        trie = {}
        for word in words:
            now = trie
            for w in reversed(word):
                if w in now:
                    now = now[w]
                else:
                    now[w] = {}
                    now = now[w]
            nodes.append(now)
        result = 0
        for word, node in zip(words, nodes):
            if len(node) == 0:
                result += len(word) + 1
        return result

# @lc code=end

