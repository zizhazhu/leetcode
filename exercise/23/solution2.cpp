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
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*>>> q;
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i]) {
                q.push(make_pair(lists[i]->val, lists[i]));
            }
        }
        while (!q.empty()) {
            ListNode *first = q.top().second;
            tail->next = first;
            q.pop();
            if (first->next) {
                q.push(make_pair(first->next->val, first->next));
            }
        }
        return head.next;
    }
};

