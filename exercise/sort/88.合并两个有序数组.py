#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        tail = m + n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                choose = 2
            elif j < 0:
                break
            elif nums1[i] < nums2[j]:
                choose = 2
            else:
                choose = 1
            if choose == 1:
                nums1[tail] = nums1[i]
                tail -= 1
                i -= 1
            else:
                nums1[tail] = nums2[j]
                tail -= 1
                j -= 1
# @lc code=end

