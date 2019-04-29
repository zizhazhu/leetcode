# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        fake = ListNode(0)
        fake.next = head
        head = fake
        while True:
            tail = head
            for i in range(k):
                tail = tail.next
                if not tail:
                    return fake.next
            for i in range(k - 1):
                head_next = head.next
                head.next = head_next.next
                head_next.next = tail.next
                tail.next = head_next
            for i in range(k):
                head = head.next
