class Solution {
public:
    void swap(vector<int>& nums, int a, int b) {
        int t = nums[a];
        nums[a] = nums[b];
        nums[b] = t;
    }

    int firstMissingPositive(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] <= 0 || nums[i] > nums.size() || nums[i] == i + 1)
                continue;
            swap(nums, i, nums[i] - 1);
            i--;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i - 1)
                return i + 1;
        }
        return nums.size();
    }
};
