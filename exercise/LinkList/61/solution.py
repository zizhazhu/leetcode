# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # special case
        if head is None:
            return head
        # k may larger than length of list
        n = 0
        tail = head
        while tail is not None:
            n += 1
            tail = tail.next
        k = k % n
        if k == 0:
            return head
        # first pointer go forward k steps
        tail = head
        for i in range(k):
            tail = tail.next
        new_tail = head
        # second pointer find new tail
        while tail.next is not None:
            new_tail = new_tail.next
            tail = tail.next
        # exchange
        tail.next = head
        head = new_tail.next
        new_tail.next = None
        return head
