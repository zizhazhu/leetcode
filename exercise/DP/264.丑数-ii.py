#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        factor_2, factor_3, factor_5 = 0, 0, 0
        while len(ugly) < n:
            a = ugly[factor_2] * 2
            b = ugly[factor_3] * 3
            c = ugly[factor_5] * 5
            result = min(a, b, c)
            ugly.append(result)
            if a == result:
                factor_2 += 1
            if b == result:
                factor_3 += 1
            if c == result:
                factor_5 += 1
        return ugly[n-1]


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(10))
