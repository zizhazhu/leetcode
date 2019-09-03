# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        now = head
        while now:
            n = now.next
            if n and n.val == now.val:
                now.next = n.next
            else:
                now = now.next
        return head
