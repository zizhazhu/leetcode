#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start

def is_palind(s, begin, end):
    i, j = begin, end - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        end = len(s)

        def part_partition(begin, result):
            if begin == end:
                results.append(list(result))
            for i in range(begin+1, end + 1):
                if is_palind(s, begin, i):
                    result.append(s[begin:i])
                    part_partition(i, result)
                    result.pop()

        if end > 0:
            part_partition(0, [])
        return results

# @lc code=end

