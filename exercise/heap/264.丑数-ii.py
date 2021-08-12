#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        h = []
        exist = set()
        heapq.heappush(h, 1)
        exist.add(1)

        last = 0
        for i in range(n):
            now = heapq.heappop(h)
            if now * 2 not in exist:
                heapq.heappush(h, now * 2)
                exist.add(now * 2)
            if now * 3 not in exist:
                heapq.heappush(h, now * 3)
                exist.add(now * 3)
            if now * 5 not in exist:
                heapq.heappush(h, now * 5)
                exist.add(now * 5)

        return now 


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(10))
