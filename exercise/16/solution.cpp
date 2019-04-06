class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int sum = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.size(); i++) {
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int s = nums[i] + nums[left] + nums[right];
                if (s == target) {
                    return s;
                } else if (abs(s - target) < abs(sum - target)) {
                    sum = s;
                }
                if (s > target) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return sum;
    }
};
