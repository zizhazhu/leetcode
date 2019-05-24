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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || k == 0) return head;
        ListNode *p = head;
        int length = 0;
        while (p) {
            length++;
            p = p->next;
        }
        int res_k = k % length;
        if (res_k == 0) return head;
        p = head;
        for (int i = 0; i < res_k; i++)
            p = p->next;
        ListNode *tail = head;
        while (p->next) {
            p = p->next;
            tail = tail->next;
        }
        p->next = head;
        head = tail->next;
        tail->next = NULL;
        return head;
    }
};
