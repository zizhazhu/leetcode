class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(a, b):
            # a first
            n = 1
            while a >= n:
                a -= n
                n += 1
                a, b = b, a
            return n - 1
        return max(height(red, blue), height(blue, red))