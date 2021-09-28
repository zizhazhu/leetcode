#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            now = letters[mid]
            if now <= target:
                left = mid + 1
            else:
                right = mid
        if letters[left] > target:
            return letters[left]
        else:
            return letters[0]

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.nextGreatestLetter(["a", "b", "k"], "j")

