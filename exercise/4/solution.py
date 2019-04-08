class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left < right:
            i = (left + right + 1) // 2
            j = (m + n + 1) // 2 - i
            if (i == 0 or nums1[i-1] <= nums2[j]) and (i == m or nums1[i] >= nums2[j-1]):
                if i == 0:
                    mid_left = nums2[j-1]
                elif j == 0:
                    mid_left = nums1[i-1]
                else:
                    mid_left = max(nums1[i-1], nums2[j-1])
                if i == m and i != 0:
                    mid_right = nums2[j]
                elif j == n:
                    mid_right = nums1[i]
                else:
                    mid_right = min(nums1[i], nums2[j])
                if (m + n) % 2 == 0:
                    return (mid_left + mid_right) / 2
                else:
                    return mid_left
            elif i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                left = i + 1
        return 0
