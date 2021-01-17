#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseN(self, head: ListNode, m: int) -> ListNode:
        if m == 1:
            return head, head.next
        next, succ = self.reverseN(head.next, m - 1)
        head.next.next = head
        head.next = succ
        return next, head.next

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            head, _ = self.reverseN(head, n)
            return head
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

# @lc code=end

