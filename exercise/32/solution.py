class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        valid = [-1 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == ')' and i - 1 >= 0:
                if s[i-1] == '(':
                    valid[i] = i - 1
                elif valid[i-1] > 0 and s[valid[i-1] - 1] == '(':
                    valid[i] = valid[i-1] - 1
                if valid[i] > 0 and valid[valid[i] - 1] >= 0:
                    valid[i] = valid[valid[i] - 1]
            if valid[i] >= 0 and i - valid[i] + 1> result:
                result = i - valid[i] + 1
        return result
