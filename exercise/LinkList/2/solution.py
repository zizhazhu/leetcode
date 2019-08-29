# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        now = ListNode(0)
        head = now
        while l1 and l2:
            c = l1.val + l2.val + carry
            now.next = ListNode(c % 10)
            carry = c // 10
            now = now.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            l = l1
        else:
            l = l2
        while l:
            c = l.val + carry
            now.next = ListNode(c % 10)
            carry = c // 10
            now = now.next
            l = l.next
        if carry > 0:
            now.next = ListNode(carry)
        return head.next
            
