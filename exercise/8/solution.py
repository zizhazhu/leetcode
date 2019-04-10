class Solution:
    def myAtoi(self, str: str) -> int:
        num_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        state = 0
        sign = 1
        num = 0
        for c in str:
            if state == 0:
                if c == ' ':
                    continue
                elif c == '+':
                    state = 1
                elif c == '-':
                    sign = -1
                    state = 1
                elif c in num_table:
                    num = num_table[c]
                    state = 1
                else:
                    break
            elif state == 1:
                if c in num_table:
                    if num > 214748365 or sign == -1 and num == 214748364 and num_table[c] > 8 or sign == 1 and num == 214748364 and num_table[c] >= 8:
                        state = 2
                        if sign == 1:
                            num = 2147483647
                        else:
                            num = 2147483648
                    else:
                        num = num * 10 + num_table[c]
                else:
                    state = 2
            elif state == 2:
                return num
        return num
