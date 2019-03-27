class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            vector<int> temp = nums2;
            nums2 = nums1;
            nums1 = temp;
        }
        int m = nums1.size(), n = nums2.size();
        int left = 0, right = m;
        while (left <= right) {
            int i = left + ((right - left) >> 1);
            int j = ((m + n + 1) >> 1) - i;
            if ((i == 0 || nums1[i-1] <= nums2[j]) && (i == m || nums1[i] >= nums2[j-1])) {
                int median_left, median_right;
                if (i == 0) {
                    median_left = nums2[j-1];
                } else if (j == 0) {
                    median_left = nums1[i-1];
                } else {
                    median_left = max(nums1[i-1], nums2[j-1]);
                }
                if (j == n) {
                    median_right = nums1[i];
                } else if (i == m) {
                    median_right = nums2[j];
                } else {
                    median_right = min(nums1[i], nums2[j]);
                }
                if ((m + n) & 1) {
                    return median_left;
                } else {
                    return (median_left + median_right) / 2.0;
                }
            } else if (i > 0 && nums1[i-1] > nums2[j]) {
                right = i - 1;
            } else if (nums1[i] < nums2[j-1]) {
                left = i + 1;
            }
        }
        return 0;
    }
};
