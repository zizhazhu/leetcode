#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fakeNode = ListNode(0, head)
        before, now = fakeNode, head
        last = fakeNode
        while now is not None:
            if now.val < x:
                if last != before:
                    before.next = now.next
                    now.next = last.next
                    last.next = now
                else:
                    before = now
                last = now
            else:
                before = before.next
            now = before.next
        return fakeNode.next
# @lc code=end

