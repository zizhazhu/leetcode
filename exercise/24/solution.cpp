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
    ListNode* swapPairs(ListNode* head) {
        ListNode fake(0);
        ListNode *point = &fake;
        fake->next = head;
        while (point->next && point->next->next) {
            ListNode *first = point->next;
            point->next = first->next;
            first->next = point->next->next;
            point->next->next = first;
            point = first->next;
        }
        return fake.next;
    }
};
