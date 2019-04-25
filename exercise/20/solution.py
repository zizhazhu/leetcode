class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if mapping[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

