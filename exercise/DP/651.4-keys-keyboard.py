class solution:
    def maxA(self, N: int) -> int:
        # default A
        answer = [i for i in range(N+1)]
        for i in range(3, N + 1):
            # Ctrl A Ctrl C Ctrl V
            for j in range(i - 3, 0, -1):
                mul = i - j - 1
                answer[i] = max(answer[i], answer[j] * mul)
        return answer[N]
