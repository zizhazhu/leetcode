class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    while (left < right && nums[right] == nums[right-1])
                        right--;
                    while (left < right && nums[left] == nums[left+1])
                        left++;
                    left++;
                    right--;
                }
            }
        }
        return result;
    }
};
