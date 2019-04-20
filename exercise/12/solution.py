class Solution:
    def intToRoman(self, num: int) -> str:
        roman = "IVXLCDM"
        result = ""
        i = 0
        while num > 0:
            digit = num % 10
            num //= 10
            now = ""
            if digit == 9:
                now = roman[i] + roman[i+2]
            elif digit >= 5:
                now = roman[i+1]
                for j in range(5, digit):
                    now += roman[i]
            elif digit == 4:
                now = roman[i] + roman[i+1]
            else:
                for j in range(0, digit):
                    now += roman[i]
            result = now + result
            i += 2
        return result
