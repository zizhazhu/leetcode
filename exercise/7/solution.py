class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            t = -x
            sign = -1
        else:
            t = x
            sign = 1
        while t != 0:
            last = t % 10
            result = result * 10 + last
            t //= 10
        result = sign * result
        if result >= 2 ** 31 or result < - 2 ** 31:
            return 0
        return result

