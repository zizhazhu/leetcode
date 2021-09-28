class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2 + 1
        while left < right:
            mid = (left + right + 1) // 2
            square_mid = mid * mid
            if square_mid == x:
                return mid
            elif square_mid < x:
                left = mid
            else:
                right = mid - 1
        return left
