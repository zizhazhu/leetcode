class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = 0;
        if (nums.empty()) return result;
        vector<int> f(nums.size());
        if (nums[0] > 0)
            f[0] = nums[0];
        else
            f[0] = 0;
        result = f[0];
        for (int i = 1; i < nums.size(); i++) {
            int now = nums[i] + f[i-1];
            if (now > 0)
                f[i] = now;
            else
                f[i] = 0;
            if (f[i] > result) result = f[i];
        }
        return result;
    }
};
