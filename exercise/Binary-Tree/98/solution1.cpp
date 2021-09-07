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
        stack<pair<TreeNode*, int>> nodes;
        nodes.push(make_pair(root, 0));
        int value;
        bool not_use = true;
        while (!nodes.empty()) {
            pair<TreeNode*, int> now = nodes.top();
            nodes.pop();
            TreeNode *node = now.first;
            if (!node) continue;
            if (now.second == 0) {
                nodes.push(make_pair(node, 1));
                nodes.push(make_pair(node->left, 0));
            } else if (now.second == 1) {
                if (not_use || node->val > value) {
                    value = node->val;
                    not_use = false;
                } else {
                    return false;
                }
                nodes.push(make_pair(node->right, 0));
            }
        }
        return true;
    }
};
