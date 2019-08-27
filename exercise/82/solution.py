# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        before = ListNode(0)
        before.next = head

        pre = before
        now = head

        remove = False

        while now:
            dup = now.next
            if dup is not None and now.val == dup.val:
                remove = True
                now.next = dup.next
            elif remove:
                pre.next = dup
                now = dup
                remove = False
            else:
                pre = pre.next
                now = now.next

        return head
