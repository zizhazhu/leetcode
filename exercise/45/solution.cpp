class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int current = 0, pre = 0, jump = 0;
        for (int i = 0; i < n; i++) {
            if (i > pre) {
                jump++;
                pre = current;
            }
            if (i + nums[i] >= n - 1)
                return jump + 1;
            if (i + nums[i] > current) {
                current = i + nums[i];
            }
        }
        return -1;
    }
};
