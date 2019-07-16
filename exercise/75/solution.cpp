class Solution {
public:
    void swap(vector<int>& nums, int a, int b) {
        if (a == b) return;
        int t = nums[a];
        nums[a] = nums[b];
        nums[b] = t;
    }
    void sortColors(vector<int>& nums) {
        if (nums.size() == 0) {
            return;
        }
        int zero_end = 0, one_end = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                swap(nums, zero_end, one_end);
                swap(nums, zero_end, i);
                zero_end++, one_end++;
            } else if (nums[i] == 1) {
                swap(nums, one_end, i);
                one_end++;
            }
        }
    }
};
