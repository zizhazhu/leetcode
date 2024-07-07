class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_x, min_y, max_x, max_y = 10000, 10000, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_x = min(min_x, i)
                    min_y = min(min_y, j)
                    max_x = max(max_x, i)
                    max_y = max(max_y, j)
        return (max_x - min_x + 1) * (max_y - min_y + 1)