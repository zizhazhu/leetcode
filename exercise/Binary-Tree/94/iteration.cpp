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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> nodes;
        while (!nodes.empty() || root) {
            while (root) {
                nodes.push(root);
                root = root->left;
            }
            root = nodes.top();
            nodes.pop();
            result.push_back(root->val);
            root = root->right;
        }
        return result;
    }
};

