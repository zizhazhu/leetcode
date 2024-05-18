// Use num cancel

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findKthElement(vector<int>& nums1, vector<int>& nums2, int k, int start1, int start2, int find2) {
        int len1 = nums1.size() - start1, len2 = nums2.size() - start2;
        if (len1 > len2) {
            return findKthElement(nums2, nums1, k, start2, start1, find2);
        }
        if (start1 >= nums1.size()) {
            if (find2 == 1) {
                return nums2[start2 + k];
            } else {
                return (nums2[start2 + k] + nums2[start2 + k + 1]) / 2.0;
            }
        }
        if (k == 0) {
            double result = min(nums1[start1], nums2[start2]);
            if (find2 == 1) {
                return result;
            } else {
                if (nums1[start1] <= nums2[start2]) {
                    return (result + findKthElement(nums1, nums2, 0, start1 + 1, start2, 1)) / 2.0;
                } else {
                    return (result + findKthElement(nums1, nums2, 0, start1, start2 + 1, 1)) / 2.0;
                }
            }
        }
        int cancel = (k + 1) / 2;
        int flag1 = min(start1 + cancel, (int)nums1.size()) - 1, flag2 = min(start2 + cancel, (int)nums2.size()) - 1;
        if (nums1[flag1] <= nums2[flag2]) {
            return findKthElement(nums1, nums2, k - (flag1 - start1 + 1), flag1 + 1, start2, find2);
        } else {
            return findKthElement(nums1, nums2, k - (flag2 - start2 + 1), start1, flag2 + 1, find2);
        }
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int k = (nums1.size() + nums2.size() - 1) / 2;
        int find2 = 2 - (nums1.size() + nums2.size()) % 2;
        return findKthElement(nums1, nums2, k, 0, 0, find2);
    }
};

int main() {
    // Case 1
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
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