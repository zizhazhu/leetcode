class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        result = 0
        last = 0
        for i in range(len(s) - 1, -1, -1):
            now = roman[s[i]]
            if roman[s[i]] < last:
                result -= now
            else:
                result += now
            last = now
        return result
