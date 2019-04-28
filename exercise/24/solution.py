# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        fake = ListNode(0)
        tail = fake
        while tail.next and tail.next.next:
            temp = tail.next
            tail.next = temp.next
            temp.next = tail.next.next
            tail.next.next = temp
            tail = temp
        return fake.next
