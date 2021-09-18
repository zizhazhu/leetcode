#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(heights), len(heights[0])
        p, w = set(), set()

        from collections import deque
        queue = deque()
        queue.append((0, 0))
        p.add((0, 0))
        for i in range(1, m):
            queue.append((i, 0))
            p.add((i, 0))
        for j in range(1, n):
            queue.append((0, j))
            p.add((0, j))

        def BFS(r_set):
            way = ((-1, 0), (1, 0), (0, -1), (0, 1))

            while len(queue) > 0:
                i, j = queue.popleft()
                for i_delta, j_delta in way:
                    new_i = i + i_delta
                    new_j = j + j_delta
                    if 0 <= new_i < m and 0 <= new_j < n and heights[new_i][new_j] >= heights[i][j] and (new_i, new_j) not in r_set:
                        queue.append((new_i, new_j))
                        r_set.add((new_i, new_j))
                    
        BFS(p)

        queue.clear()
        queue.append((m - 1, n - 1))
        w.add((m - 1, n - 1))
        for i in range(0, m - 1):
            queue.append((i, n - 1))
            w.add((i, n - 1))
        for j in range(0, n - 1):
            queue.append((m - 1, j))
            w.add((m - 1, j))
        BFS(w)
        for x, y in p:
            if (x, y) in w:
                result.append([x, y])
        return result
# @lc code=end

