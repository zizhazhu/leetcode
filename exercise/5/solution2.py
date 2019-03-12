class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palind = [[False for __ in range(len(s))] for _ in range(len(s))]
        max_length = 1
        left = 0
        for i in range(len(s)):
            j = i
            # from j to i(include j and i)
            while j >= 0:
                if s[i] == s[j] and (i - j < 2 or is_palind[i-1][j+1]):
                    is_palind[i][j] = True
                    if i - j + 1 > max_length:
                        max_length = i - j + 1
                        left = j
                j -= 1
        return s[left:left+max_length]
