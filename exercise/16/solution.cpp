class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int sum = 2000000000;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int res = target - nums[i] - nums[j];
                vector<int>::iterator it = lower_bound(nums.begin(), nums.end(), res);
                for (auto it_r = it; it_r != nums.end(); it_r++) {
                    int s = nums[i] + nums[j] + *it_r;
                    if (abs(s - target) > abs(sum - target)) {
                        break;
                    } else if (it_r - nums.begin() == i || it_r - nums.begin() == j) {
                        continue;
                    } else {
                        sum = s;
                        break;
                    }
                }
                for (int k = it - nums.begin() - 1; k >= 0; k--) {
                    int s = nums[i] + nums[j] + nums[k];
                    if (abs(s - target) > abs(sum - target)) {
                        break;
                    } else if (k == i || k == j) {
                        continue;
                    } else {
                        sum = s;
                        break;
                    }
                }
            }
        }
        return sum;
    }
};
