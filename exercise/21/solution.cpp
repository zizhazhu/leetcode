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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head = NULL;
        ListNode **p = &head;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                *p = l1;
                l1 = l1->next;
            } else {
                *p = l2;
                l2 = l2->next;
            }
            p = &((*p)->next);
        }
        if (l1 == NULL) {
            *p = l2;
        } else if (l2 == NULL) {
            *p = l1;
        }
        return head;
    }
};
