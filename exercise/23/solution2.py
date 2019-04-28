# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        head = ListNode(0)
        tail = head
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        while len(heap) > 0:
            no = heap[0][1]
            heappop(heap)
            tail.next = lists[no]
            lists[no] = lists[no].next
            if lists[no]:
                heappush(heap, (lists[no].val, no))
            tail = tail.next
        return head.next
        
