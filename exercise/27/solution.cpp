class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int tail = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[tail] = nums[i];
                tail++;
            }
        }
        return tail;
    }
};
