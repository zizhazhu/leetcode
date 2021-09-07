#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_num = [1]
        progress = [0 for _ in range(len(primes))]
        while len(ugly_num) < n:
            nums = []
            for i in range(len(primes)):
                nums.append(primes[i] * ugly_num[progress[i]])
            smallest = min(nums)
            for i in range(len(primes)):
                if nums[i] == smallest:
                    progress[i] += 1
            ugly_num.append(smallest)
                
        return ugly_num[-1]

# @lc code=end

