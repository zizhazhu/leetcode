class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        is_palind = [[False for __ in range(len(s))] for _ in range(len(s))]
        max_length = 1
        left, right = 0, 0
        for i in range(len(s)):
            j = i
            # from j to i(include j and i)
            while j >= 0:
                if s[i] == s[j] and (i - j < 2 or is_palind[i-1][j+1]):
                    is_palind[i][j] = True
                    if i - j + 1 > max_length:
                        max_length = i - j + 1
                        left = j
                        right = i
                j -= 1
        return s[left:right+1]
