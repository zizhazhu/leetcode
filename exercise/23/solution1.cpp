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
    ListNode* merge2Lists(ListNode* list1, ListNode* list2) {
        // a fake head
        ListNode head(0);
        ListNode *tail = &head;
        while (list1 && list2) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
                tail = tail->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
                tail = tail->next;
            }
        }
        if (list1) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }
        return head.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return NULL;
        }
        for (int gap = 1; gap < lists.size(); gap *= 2) {
            for (int k = 0; k + gap < lists.size(); k += gap * 2) {
                lists[k] = merge2Lists(lists[k], lists[k+gap]);
            }
        }
        return lists[0];
    }
};
