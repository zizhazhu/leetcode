class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = [""]
        for c in digits:
            new_result = []
            for prefix in result:
                for next_c in phone[c]:
                    new_result.append(prefix + next_c)
            result = new_result
        return result

