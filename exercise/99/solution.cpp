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
                    if (first)
                        second = cur;
                    else {
                        first = pre;
                        second = cur;
                    }
                }
                pre = cur;
                cur = cur->right;
                continue;
            }
            pre = cur->left;
            while (pre->right && pre->right != cur) {
                pre = pre->right;
            }
            if (pre->right == cur) {
                pre->right = NULL;
                if (pre && cur->val < pre->val) {
                    if (first)
                        second = cur;
                    else {
                        first = pre;
                        second = cur;
                    }
                }
                pre = cur;
                cur = cur->right;
            } else {
                pre->right = cur;
                pre = cur;
                cur = cur->left;
            }
        }
        int t = first->val;
        first->val = second->val;
        second->val = t;
    }
};
