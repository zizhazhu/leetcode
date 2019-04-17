class Solution {
public:
    void swap(vector<int>& nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    void reverse(vector<int>& nums, int i, int j) {
        for (int k = 0; k < (j - i + 1) / 2; k++) {
            swap(nums, i + k, j - k);
        }
    }

    void nextPermutation(vector<int>& nums) {
        if (nums.size() == 0 || nums.size() == 1) {
            return;
        }
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                int j = i + 1;
                for (; j < nums.size(); j++) {
                    if (nums[j] < nums[i])
                        break;
                }
                swap(nums, i, j - 1);
                reverse(nums, i + 1, nums.size() - 1);
                break;
            }
        }
    }
};
