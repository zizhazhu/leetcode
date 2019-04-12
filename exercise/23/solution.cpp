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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // a fake head
        ListNode head(0);
        ListNode *tail = &head;
        int last = -2147483648;
        bool exist = true;
        while (exist) {
            exist = false;
            int min = 2147483647, no = -1;
            for (int i = 0; i < lists.size(); i++) {
                if (lists[i]) {
                    exist = true;
                    if (lists[i]->val == last) {
                        tail->next = lists[i];
                        lists[i] = lists[i]->next;
                        tail = tail->next;
                        tail->next = NULL;
                    } else {
                        if (lists[i]->val < min) {
                            min = lists[i]->val;
                            no = i;
                        }
                    }
                }
            }
            if (no != -1) {
                tail->next = lists[no];
                lists[no] = lists[no]->next;
                tail = tail->next;
                tail->next = NULL;
                last = min;
            }
        }
        return head.next;
    }
};
