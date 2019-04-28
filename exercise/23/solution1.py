# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, list_a: ListNode, list_b: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        while list_a and list_b:
            if list_a.val < list_b.val:
                tail.next = list_a
                list_a = list_a.next
            else:
                tail.next = list_b
                list_b = list_b.next
            tail = tail.next
        if list_a:
            tail.next = list_a
        else:
            tail.next = list_b
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        gap = 1
        while gap < len(lists):
            for i in range(0, len(lists) - gap, gap * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+gap])
            gap *= 2
        return lists[0]
        
