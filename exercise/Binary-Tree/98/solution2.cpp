/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<pair<TreeNode*, pair<long, long>>> nodes;
        nodes.push(make_pair(root, make_pair(LONG_MIN, LONG_MAX)));
        while (!nodes.empty()) {
            auto now = nodes.top();
            nodes.pop();
            TreeNode *p = now.first;
            if (!p) continue;
            auto limit = now.second;
            if (p->val <= limit.first || p->val >= limit.second) return false;
            nodes.push(make_pair(p->left, make_pair(limit.first, p->val)));
            nodes.push(make_pair(p->right, make_pair(p->val, limit.second)));
        }
        return true;
    }
};
