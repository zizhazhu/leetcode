#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = numbers.pop()
                a = numbers.pop()
                if token == '+':
                    r = a + b
                elif token == '-':
                    r = a - b
                elif token == '*':
                    r = a * b
                elif  token == '/':
                    r = int(a / b)
                numbers.append(r)
            else:
                numbers.append(int(token))
        return numbers[0]

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
