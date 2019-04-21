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
        TreeNode *now = root;
        while (now) {
            if (!now->left) {
                result.push_back(now->val);
                now = now->right;
                continue;
            }
            TreeNode *pre = now->left;
            while (pre->right && pre->right != now) {
                pre = pre->right;
            }
            if (pre->right != now) {
                pre->right = now;
                now = now->left;
            } else {
                pre->right = NULL;
                result.push_back(now->val);
                now = now->right;
            }
        }
        return result;
    }
};
