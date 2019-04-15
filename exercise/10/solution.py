class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        meet = [[False for i in range(n+1)] for j in range(m+1)]
        meet[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                same = i < m and (s[i] == p[j] or p[j] == '.')
                if j + 1 < n and p[j+1] == '*':
                    meet[i][j] = meet[i][j+2] or same and meet[i+1][j]
                else:
                    meet[i][j] = same and meet[i+1][j+1]
        return meet[0][0]

