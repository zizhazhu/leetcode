class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        first_line, first_col = False, False
        for i in range(n):
            if matrix[0][i] == 0:
                first_line = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        if first_line:
            for i in range(n):
                matrix[0][i] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
