class Solution {
public:
    void dfs(vector<int> &candidates, int index, int res, vector<vector<int>> &result, vector<int> &now) {
        if (res == 0) {
            result.push_back(now);
            return;
        }
        if (candidates[index] > res) {
            return;
        } else {
            now.push_back(candidates[index]);
            dfs(candidates, index, res - candidates[index], result, now);
            now.pop_back();
            if (index < candidates.size() - 1)
                dfs(candidates, index + 1, res, result, now);
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> candidates_dup(candidates);
        sort(candidates_dup.begin(), candidates_dup.end());
        candidates_dup.erase(unique(candidates_dup.begin(), candidates_dup.end()), candidates_dup.end());
        vector<vector<int>> result;
        vector<int> now;
        dfs(candidates_dup, 0, target, result, now);
        return result;
    }
};
