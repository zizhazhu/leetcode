class Solution {
public:
    bool canJump(vector<int>& nums) {
        int range = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > range)
                return false;
            if (i + nums[i] >= nums.size())
                return true;
            else if (i + nums[i] > range)
                range = i + nums[i];
        }
        return true;
    }
};
