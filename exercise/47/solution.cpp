class Solution {
public:
    void permutePart(vector<vector<int>> &result, vector<int> &now, vector<bool> &reached, vector<int> &nums) {
        if (now.size() == nums.size()) {
            result.push_back(now);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (!reached[i]) {
                if (i > 0 && nums[i] == nums[i-1] && !reached[i-1])
                    continue;
                now.push_back(nums[i]);
                reached[i] = true;
                permutePart(result, now, reached, nums);
                reached[i] = false;
                now.pop_back();
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.empty()) return result;
        sort(nums.begin(), nums.end());
        vector<int> now;
        vector<bool> reached(nums.size());
        permutePart(result, now, reached, nums);
        return result;
    }
};
