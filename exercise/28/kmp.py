class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if n > m:
            return -1
        move = [0 for _ in range(n + 1)]
        move[0] = -1
        i, j = 0, -1
        while i <= n and j <= n:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                move[i] = j
            else:
                j = move[j]
        i, j = 0, 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = move[j]
        if j == n:
            return i - j
        else:
            return -1
