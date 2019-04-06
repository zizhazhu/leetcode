class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        map<int, vector<pair<int, int>>> two_sum;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int sum = nums[i] + nums[j];
                two_sum[sum].push_back(make_pair(i, j));
            }
        }
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++) {
            vector<pair<int, int>> &target = two_sum[-nums[i]];
            for (int j = 0; j < target.size(); j++) {
                if (target[j].first > i && target[j].second > j) {
                    vector<int> now;
                    now.push_back(nums[i]);
                    now.push_back(nums[target[j].first]);
                    now.push_back(nums[target[j].second]);
                    result.push_back(now);
                }
            }
        }
        vector<int>::iterator iter = unique(result.begin(), result.end());
        result.erase(iter, result.end());
        return result;
    }
};
