from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        results = 0
        x_s = [[0] * n for _ in range(m)]
        y_s = [[0] * n for _ in range(m)]

        if grid[0][0] == 'X':
            x_s[0][0] = 1
        if grid[0][0] == 'Y':
            y_s[0][0] = 1

        for j in range(1, n):
            if grid[0][j] == 'X':
                x_s[0][j] = x_s[0][j - 1] + 1
            else:
                x_s[0][j] = x_s[0][j - 1]
            if grid[0][j] == 'Y':
                y_s[0][j] = y_s[0][j - 1] + 1
            else:
                y_s[0][j] = y_s[0][j - 1]
            if x_s[0][j] == y_s[0][j] and x_s[0][j] > 0:
                results += 1

        for i in range(1, m):
            if grid[i][0] == 'X':
                x_s[i][0] = x_s[i - 1][0] + 1
            else:
                x_s[i][0] = x_s[i - 1][0]
            if grid[i][0] == 'Y':
                y_s[i][0] = y_s[i - 1][0] + 1
            else:
                y_s[i][0] = y_s[i - 1][0]
            if x_s[i][0] == y_s[i][0] and x_s[i][0] > 0:
                results += 1

            for j in range(1, n):
                if grid[i][j] == 'X':
                    x_s[i][j] = x_s[i-1][j] + x_s[i][j-1] - x_s[i-1][j-1] + 1
                else:
                    x_s[i][j] = x_s[i-1][j] + x_s[i][j-1] - x_s[i-1][j-1]
                if grid[i][j] == 'Y':
                    y_s[i][j] = y_s[i-1][j] + y_s[i][j-1] - y_s[i-1][j-1] + 1
                else:
                    y_s[i][j] = y_s[i-1][j] + y_s[i][j-1] - y_s[i-1][j-1]
                if x_s[i][j] == y_s[i][j] and x_s[i][j] > 0:
                    results += 1
        return results


grid = [["X","Y","."],["Y",".","."]]
solution = Solution()
print(solution.numberOfSubmatrices(grid))  # 1