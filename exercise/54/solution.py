class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        if m == 0:
            return result
        n = len(matrix[0])
        if n == 0:
             return result
        reached = [[False for __ in range(len(matrix[0]))] for _ in range(len(matrix))]
        x, y = 0, 0
        way = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        while len(result) < m * n:
            result.append(matrix[x][y])
            reached[x][y] = True
            next_x, next_y = x + way[d][0], y + way[d][1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or reached[next_x][next_y]:
                d = (d + 1) % 4
            x, y = x + way[d][0], y + way[d][1]
        return result

