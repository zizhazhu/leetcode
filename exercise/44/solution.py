class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = [False for i in range(len(s) + 1)]
        match[0] = True
        pre = False
        for i in range(len(s) + 1):
            pre = match[0]
            if i != 0:
                match[0] = False
            for j in range(1, len(p) + 1):
                new_pre = match[j]
                match[j] = False
                if pre and i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                    match[j] = True
                elif match[j-1] and p[j-1] == '*':
                    match[j] = True
                elif i > 0 and new_pre and p[j-1] == '*':
                    match[j] = True
                pre = new_pre
        return match[p+1]


