from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        results = []
        str_list = ["0"] * n

        while True:
            valid = True
            for i in range(1, n):
                if str_list[i] != "1" and str_list[i - 1] != "1":
                    valid = False
                    break
            if valid:
                results.append("".join(str_list))
            j = n - 1
            while j >= -1:
                if j == -1:
                    return results
                if str_list[j] == "0":
                    str_list[j] = "1"
                    break
                else:
                    str_list[j] = "0"
                    j -= 1
