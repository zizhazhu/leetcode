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

        def BFS(x, y):
            from collections import deque
            queue = deque()
            reached = set()
            queue.append((x, y))
            reached.add((x, y))
            way = ((-1, 0), (1, 0), (0, -1), (0, 1))
            p, w = False, False

            while len(queue) > 0:
                if p and w:
                    return p, w
                i, j = queue.popleft()
                if i == 0 or j == 0:
                    p = True
                if i == m - 1 or j == n - 1:
                    w = True
                for i_delta, j_delta in way:
                    new_i = i + i_delta
                    new_j = j + j_delta
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and heights[new_i][new_j] <= heights[i][j] and (new_i, new_j) not in reached:
                        queue.append((new_i, new_j))
                        reached.add((new_i, new_j))
                    
            return p, w

        for i in range(m):
            for j in range(n):
                p, w = BFS(i, j)
                if p and w:
                    result.append([i, j])

        return result
# @lc code=end

