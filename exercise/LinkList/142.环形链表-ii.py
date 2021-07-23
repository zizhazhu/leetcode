#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        holder = ListNode(-1)
        holder.next = head
        slow, fast = holder, holder
        while slow is not None and fast is not None and (slow == holder or slow != fast):
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
        if slow is None or fast is None:
            return None
        fast = holder
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
        
# @lc code=end

