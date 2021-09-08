#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#
from collections import deque

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        queue = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        while queue:
            result = list()
            size = len(queue)
            for i in range(size):
                now = queue.popleft()
                result.append(now)
                for node in graph[now]:
                    graph[node].remove(now)
                    if len(graph[node]) == 1:
                        queue.append(node)

        return result
        

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])