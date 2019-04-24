# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        for _ in range(n + 1):
            first = first.next
        second = dummy
        while first:
            second = second.next
            first = first.next
        second.next = second.next.next
        return dummy.next
