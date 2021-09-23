class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        left, right = 0, m
        while left < right - 1:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid
            else:
                right = mid
        row = left
        if row == m:
            return False
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid
        return False
