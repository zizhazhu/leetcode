class Solution:
    cache = {0: [""]}
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        if n in self.cache:
            return self.cache[n]
        for i in range(n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n - i - 1)
            for j in range(len(left)):
                for k in range(len(right)):
                    result.append('(' + left[j] + ')' + right[k])
        self.cache[n] = result
        return result

