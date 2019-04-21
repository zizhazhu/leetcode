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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<pair<TreeNode*, int>> nodes;
        nodes.push(make_pair(root, 0));
        while (!nodes.empty()) {
            auto now = nodes.top();
            nodes.pop();
            TreeNode *p = now.first;
            if (!p) continue;
            int state = now.second;
            if (state == 0) {
                nodes.push(make_pair(p, 1));
                nodes.push(make_pair(p->right, 0));
                nodes.push(make_pair(p->left, 0));
            } else {
                result.push_back(p->val);
            }
        }
        return result;
    }
};
