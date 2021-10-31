class Solution:
    def findNQueens(self, n: int, level: int, col: set, left_up: set, left_down: set) -> int:
        if level == n:
            return 1
        result = 0
        for i in range(n):
            if i not in col and level - i not in left_up and level + i not in left_down:
                col.add(i)
                left_up.add(level - i)
                left_down.add(level + i)
                result += self.findNQueens(n, level + 1, col, left_up, left_down)
                left_down.remove(level + i)
                left_up.remove(level - i)
                col.remove(i)
        return result
        

    def totalNQueens(self, n: int) -> int:
        return self.findNQueens(n, 0, set(), set(), set())
