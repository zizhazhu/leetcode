class Solution {
public:
    void permuteN(vector<vector<int>> &result, vector<int> &now, vector<bool> &reached, vector<int> &nums) {
        if (now.size() == nums.size()) result.push_back(now);
        for (int i = 0; i < nums.size(); i++) {
            if (reached[i]) continue;
            now.push_back(nums[i]);
            reached[i] = true;
            permuteN(result, now, reached, nums);
            reached[i] = false;
            now.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.empty()) return result;
        vector<int> now;
        vector<bool> reached(nums.size());
        permuteN(result, now, reached, nums);
        return result;
    }
};
