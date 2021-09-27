#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq
        num_counter = {}
        num_stats = []

        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1
        
        for num, counter in num_counter.items():
            heapq.heappush(num_stats, (-counter, num))
        
        result = []
        for i in range(k):
            _, num = heapq.heappop(num_stats)
            result.append(num)

        return result


# @lc code=end

