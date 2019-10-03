/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dum(0);
        ListNode *pre, *first, *second;
        dum.next = head;
        pre = &dum, first = head;
        bool dup = false;
        while (first) {
            second = first->next;
            if (second && first->val == second->val) {
                first->next = second->next;
                delete second;
                second = first->next;
                dup = true;
            } else if (dup) {
                pre->next = second;
                delete first;
                first = pre->next;
            } else {
                pre = first;
                first = second;
            }
        }
        return dum.next;
    }
};
