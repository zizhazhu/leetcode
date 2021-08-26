class Solution {
public:
    void swap(vector<int> &nums, int a, int b) {
        int t = nums[a];
        nums[a] = nums[b];
        nums[b] = t;
    }

    int quick(vector<int> &nums, int k, int begin, int end) {
        if (begin == end - 1)
            return nums[begin];
        int q = nums[end-1];
        int left = begin;
        for (int i = begin; i < end - 1; i++) {
            if (nums[i] > q) {
                swap(nums, i, left);
                left++;
            }
        }
        swap(nums, end - 1, left);
        if (left == k) {
            return nums[left];
        } else if (left < k) {
            return quick(nums, k, left + 1, end);
        } else {
            return quick(nums, k, 0, left);
        }
    }

    int findKthLargest(vector<int>& nums, int k) {
        return quick(nums, k - 1, 0, nums.size());
    }
};
