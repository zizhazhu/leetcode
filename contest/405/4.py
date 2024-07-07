from typing import List
from functools import cache


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        words_dict = {}
        for i in range(len(words)):
            node = words_dict
            for c in words[i]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            if 'cost' not in node:
                node['cost'] = 100000000
            node['cost'] = min(node['cost'], costs[i])

        @cache
        def split(target):
            if target == '':
                return 0
            result = 100000000
            node = words_dict
            for i in range(len(target)):
                if target[i] not in node:
                    break
                node = node[target[i]]
                if 'cost' in node and node['cost'] < 100000000:
                    result = min(result, node['cost'] + split(target[i + 1:]))
            return result

        r = split(target)
        if r == 100000000:
            return -1
        else:
            return r

solution = Solution()
print(solution.minimumCost("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5]))  # 1