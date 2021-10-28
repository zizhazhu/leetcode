#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmid(self, head):
        if not head.next:
            return head
        first = ListNode(-1, head)
        fast = slow = first
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        ret = slow.next
        slow.next = None
        return ret

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findmid(head)
        head = self.sortList(head)
        mid = self.sortList(mid)
        ret = ListNode(-1)
        now = ret
        while head and mid:
            if head.val < mid.val:
                now.next = head
                head = head.next
            else:
                now.next = mid
                mid = mid.next
            now = now.next
        if head:
            now.next = head
        if mid:
            now.next = mid
        return ret.next
        
# @lc code=end

