class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > k_largest;
        for (int i = 0; i < nums.size(); i++) {
            if (k_largest.size() == k) {
                if (k_largest.top() < nums[i]) {
                    k_largest.pop();
                }
            }
            if (k_largest.size() < k) {
                k_largest.push(nums[i]);
            }
        }
        return k_largest.top();
    }
};
