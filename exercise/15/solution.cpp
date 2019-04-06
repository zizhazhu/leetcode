class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                if (nums[i] + nums[left] + nums[right] == 0) {
                    vector<int> now;
                    now.push_back(nums[i]);
                    now.push_back(nums[left]);
                    now.push_back(nums[right]);
                    result.push_back(now);
                    left++;
                    right--;
                }
                while (nums[i] + nums[left] + nums[right] > 0 || (right < nums.size() - 1 && nums[right] ==  nums[right+1])) {
                    right--;
                }
                while (nums[i] + nums[left] + nums[right] < 0 || (left > i + 1 && nums[left] ==  nums[left-1])) {
                    left++;
                }
            }
        }
        return result;
    }
};
