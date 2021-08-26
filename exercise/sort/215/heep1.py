class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue
        heap = PriorityQueue()
        for num in nums:
            if heap.qsize() == k:
                if heap.queue[0] < num:
                    heap.get()
            if heap.qsize() < k:
                heap.put(num)
        return heap.get()
