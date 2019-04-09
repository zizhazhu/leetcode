class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        gap = numRows * 2 - 2
        result = ""
        for i in range(0, len(s), gap):
            result += s[i]
        for i in range(1, numRows - 1):
            for j in range(i, len(s), gap):
                result += s[j]
                if j + gap - 2 * i < len(s):
                    result += s[j + gap - 2 * i]
        for i in range(numRows - 1, len(s), gap):
            result += s[i]
        return result
