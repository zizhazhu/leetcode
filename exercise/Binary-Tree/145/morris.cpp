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
    void reverse(vector<int> &result, int left, int right) {
        for (int i = 0; i < (right - left) / 2; i++) {
            int t = result[left + i];
            result[left+i] = result[right-i-1];
            result[right-i-1] = t;
        }
    }
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode fake(0);
        fake.left = root;
        TreeNode *p = &fake;
        while (p) {
            if (!p->left) {
                p = p->right;
                continue;
            }
            TreeNode *pre = p->left;
            while (pre->right && pre->right != p) {
                pre = pre->right;
            }
            if (pre->right == p) {
                pre->right = NULL;
                int a = result.size();
                pre = p->left;
                while (pre) {
                    result.push_back(pre->val);
                    pre = pre->right;
                }
                reverse(result, a, result.size());
                p = p->right;
            } else {
                pre->right = p;
                p = p->left;
            }
        }
        return result;
    }
};

