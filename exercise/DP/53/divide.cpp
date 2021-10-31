class Solution {
public:
    void maxSubArrayPart(vector<int>& nums, int from, int to, int &mx, int &left, int &right, int &sum) {
        if (from == to) {
            mx = left = right = sum = nums[from];
        } else {
        int left_mx, left_left, left_right, left_sum;
        int right_mx, right_left, right_right, right_sum;
        int middle = from + (to - from) / 2;
        maxSubArrayPart(nums, from, middle, left_mx, left_left, left_right, left_sum);
        maxSubArrayPart(nums, middle + 1, to, right_mx, right_left, right_right, right_sum);
        mx = max({left_mx, right_mx, left_right + right_left});
        left = max(left_left, left_sum + right_left);
        right = max(right_right, left_right + right_sum);
        sum = left_sum + right_sum;
        }
    }

    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) return 0;
        int left, right, sum, mx;
        maxSubArrayPart(nums, 0, nums.size() - 1, mx, left, right, sum);
        return mx;
    }
};

