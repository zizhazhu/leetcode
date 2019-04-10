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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) {
            return head;
        }
        ListNode **pri = &head, **now = &head;
        for (int i = 0; i < n; i++) {
            pri = &((*pri)->next);
        }
        while (*pri) {
            now = &(*now)->next;
            pri = &(*pri)->next;
        }
        ListNode *temp = *now;
        *now = (*now)->next;
        delete temp;
        return head;
    }
};
