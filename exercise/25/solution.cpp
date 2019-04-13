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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) {
            return head;
        }
        ListNode fake = ListNode(0);
        ListNode *point = &fake;
        point->next = head;
        while (true) {
            ListNode *last = point, *first;
            bool done = false;
            for (int i = 0; i < k; i++) {
                if (last->next) {
                    last = last->next;
                } else {
                    done = true;
                    break;
                }
            }
            if (done)
                break;
            for (int i = 0; i < k - 1; i++) {
                last = point->next;
                first = last->next;
                last->next = first->next;
                first->next = point->next;
                point->next = first;
            }
            point = last;
        }
        return fake.next;
    }
};
