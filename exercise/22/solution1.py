class Solution:
    def generate(self, result: List[str], left: int, right: int, remain: int, now: str):
        if left > right:
            self.generate(result, left, right + 1, remain, now + ')')
        if left < remain:
            self.generate(result, left + 1, right, remain, now + '(')
        if left == right and left == remain:
            result.append(now)

    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        self.generate(result, 0, 0, n, "")
        return result

