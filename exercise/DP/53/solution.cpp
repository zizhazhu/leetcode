class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = 0;
        if (nums.empty()) return result;
        vector<int> f(nums.size());
        f[0] = nums[0];
        result = f[0];
        for (int i = 1; i < nums.size(); i++) {
            if (f[i-1] > 0)
                f[i] = f[i-1] + nums[i];
            else
                f[i] = nums[i];
            if (f[i] > result) result = f[i];
        }
        return result;
    }
};
