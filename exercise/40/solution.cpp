class Solution {
public:
    void dfs (vector<vector<int>> &result, vector<int> &now, int res, vector<pair<int, int>> &nums, int index) {
        if (res == 0) {
            result.push_back(now);
            return;
        }
        if (nums[index].first > res) return;
        if (index + 1 < nums.size()) {
            dfs(result, now, res, nums, index + 1);
        }
        if (nums[index].second > 0) {
            now.push_back(nums[index].first);
            nums[index].second--;
            dfs(result, now, res - nums[index].first, nums, index);
            nums[index].second++;
            now.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        if (candidates.empty()) return result;
        sort(candidates.begin(), candidates.end());
        vector<pair<int, int>> nums;
        nums.push_back(make_pair(candidates[0], 1));
        for (int i = 1; i < candidates.size(); i++) {
            if (candidates[i] == nums.back().first) {
                nums.back().second++;
            } else {
                nums.push_back(make_pair(candidates[i], 1));
            }
        }
        vector<int> now;
        dfs(result, now, target, nums, 0);
        return result;
    }
};
