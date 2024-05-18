// Use binary search in two array

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    int length = nums1.size() + nums2.size();
    int k = (length + 1) / 2;
    int left = max(0, k - (int)nums2.size()), right = min((int)nums1.size(), k);
    while (left < right) {
      int mid = left + (right - left) / 2;
      int mid2 = k - mid;
      if (mid > 0 && mid2 < nums2.size() && nums1[mid - 1] > nums2[mid2]) {
        right = mid - 1;
      } else if (mid2 > 0 && mid < nums1.size() &&
                 nums2[mid2 - 1] > nums1[mid]) {
        left = mid + 1;
      } else {
        left = right = mid;
      }
    }
    int first, second;
    if (left == 0) {
        first = nums2[k - 1];
    } else if (k - left == 0) {
        first = nums1[left - 1];
    } else {
        first = max(nums1[left-1], nums2[k-left-1]);
    }
    if (length % 2 == 0) {
        if (left == nums1.size()) {
            second = nums2[k - left];
        } else if (k - left == nums2.size()) {
            second = nums1[left];
        } else {
            second = min(nums1[left], nums2[k-left]);
        }
    } else {
        second = first;
    }
    return (first + second) / 2.0;
  }
};

int main() {
    // Case 0
    vector<int> nums1 = {2};
    vector<int> nums2 = {};
    // Expected output: 2.0
    cout << Solution().findMedianSortedArrays(nums1, nums2) << endl;

    // Case 1
    nums1 = {1, 3};
    nums2 = {2};
    // Expected output: 2.0
    cout << Solution().findMedianSortedArrays(nums1, nums2) << endl;

    // Case 2
    nums1 = {1, 2};
    nums2 = {3, 4};
    // Expected output: 2.5
    cout << Solution().findMedianSortedArrays(nums1, nums2) << endl;

    // Case 3
    nums1 = {1};
    nums2 = {2, 3, 4, 5, 6, 7};
    cout << Solution().findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}