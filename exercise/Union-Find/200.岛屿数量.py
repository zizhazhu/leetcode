#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:

    def find_root(self, a):
        if self.root[a] == a:
            return a
        self.root[a] = self.find_root(self.root[a])
        return self.root[a]

    def merge(self, a, b):
        self.root[self.find_root(b)] = a

    def union(self, a, b):
        a_root, b_root = self.find_root(a), self.find_root(b)
        if a_root != b_root:
            self.merge(a, b)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.root = [i for i in range(m*n)]
        ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def trans(i, j):
            return i * n + j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for way in ways:
                        new_i, new_j = i + way[0], j + way[1]
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
                            self.union(trans(i, j), trans(new_i, new_j))
        
        count = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count.add(self.find_root(trans(i, j)))
        
        return len(count)


# @lc code=end
