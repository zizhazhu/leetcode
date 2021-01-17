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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        fake_head = ListNode(-1)
        rever_head = fake_head
        rever_head.next = head
        for i in range(0, m - 1):
            rever_head = rever_head.next
        tail = rever_head.next
        out_head = None
        for i in range(0, n - m + 1):
            rever_head_next = rever_head.next
            rever_head.next = rever_head_next.next
            rever_head_next.next = out_head
            out_head = rever_head_next
        tail.next = rever_head.next
        rever_head.next = out_head
        return fake_head.next

# @lc code=end

