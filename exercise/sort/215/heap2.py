class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            if len(heap) == k:
                if heap[0] < num:
                    heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, num)
        return heap[0]

