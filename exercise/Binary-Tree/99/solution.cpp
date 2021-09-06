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
    void recoverTree(TreeNode* root) {
        TreeNode *first = NULL, *second = NULL;
        TreeNode *pre = NULL, *cur = root;
        while (cur) {
            if (!cur->left) {
                if (pre && cur->val < pre->val) {
                    if (!first)
                        first = pre;
                    second = cur;
                }
                pre = cur;
                cur = cur->right;
                continue;
            }
            TreeNode *pre_pre = cur->left;
            while (pre_pre->right && pre_pre->right != cur) {
                pre_pre = pre_pre->right;
            }
            if (pre_pre->right == cur) {
                pre_pre->right = NULL;
                if (pre && cur->val < pre->val) {
                    if (!first)
                        first = pre;
                    second = cur;
                }
                pre = cur;
                cur = cur->right;
            } else {
                pre_pre->right = cur;
                cur = cur->left;
            }
        }
        int t = first->val;
        first->val = second->val;
        second->val = t;
    }
};
