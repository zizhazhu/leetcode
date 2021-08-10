class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        result = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c not in count or count[c] == 0:
                count[c] = 1
            else:
                count[c] += 1
                while left < right:
                    c_left = s[left]
                    count[c_left] -= 1
                    left += 1
                    if count[c_left] == 1:
                        break
            if result < right - left + 1:
                result = right - left + 1
        return result

