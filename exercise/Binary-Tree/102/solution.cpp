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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        queue<pair<TreeNode*, int>> fifo;
        fifo.push(make_pair(root, 0));
        int level = 0;
        vector<int> level_result;
        while (!fifo.empty()) {
            pair<TreeNode*, int> now = fifo.front();
            fifo.pop();
            TreeNode* node = now.first;
            if (now.second != level) {
                result.push_back(level_result);
                level_result.clear();
                level++;
            }
            level_result.push_back(node->val);
            if (node->left)
                fifo.push(make_pair(node->left, now.second + 1));
            if (node->right)
                fifo.push(make_pair(node->right, now.second + 1));
        }
        result.push_back(level_result);
        return result;
    }
};
