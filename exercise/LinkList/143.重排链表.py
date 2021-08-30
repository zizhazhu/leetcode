#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode) -> None:
        prev = None
        now = head
        while now is not None:
            t = now.next
            now.next = prev
            prev = now
            now = t
        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        base = ListNode(-1, head)
        fast, slow = base, base
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
        base2 = slow.next
        slow.next = None
        base2 = self.reverse(base2)
        fast = base.next
        slow = base2
        while slow is not None:
            t = slow
            slow = slow.next
            t.next = fast.next
            fast.next = t
            fast = t.next

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    a = ListNode(2, None)
    a = ListNode(1, a)
    s.reorderList(a)


