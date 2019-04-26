# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode(0)
        now = fake
        while l1 and l2:
            if l1.val < l2.val:
                now.next = l1
                l1 = l1.next
            else:
                now.next = l2
                l2 = l2.next
            now = now.next
        if l1 is None:
            now.next = l2
        else:
            now.next = l1
        return fake.next
