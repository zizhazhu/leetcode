#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return None

        def reverse(l):
            l_r = ListNode(-1)
            while l:
                t = l
                l = l.next
                t.next = l_r.next
                l_r.next = t
            return l_r.next
        
        l1_r = reverse(l1)
        l2_r = reverse(l2)

        result = ListNode(-1)
        carry = 0
        while l1_r or l2_r:
            if l1_r:
                l1_v = l1_r.val
                l1_r = l1_r.next
            else:
                l1_v = 0
            if l2_r:
                l2_v = l2_r.val
                l2_r = l2_r.next
            else:
                l2_v = 0
            r = l1_v + l2_v + carry
            if r >= 10:
                carry = 1
                r = r - 10
            else:
                carry = 0
            result.next = ListNode(r, result.next)
        if carry == 1:
            result.next = ListNode(1, result.next)
        return result.next
# @lc code=end

