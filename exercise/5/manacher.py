class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_trans = '#'
        for i in range(0, len(s)):
            s_trans += s[i]
            s_trans += '#'
        length = [0 for _ in range(len(s_trans))]
        max_length = 0
        max_mid = 0
        center = 0
        right = 0
        for i in range(1, len(s_trans)):
            if i >= right:
                length[i] = 0
            else:
                length[i] = min(right - i, length[2 * center - i])
            while i - length[i] - 1 >= 0 and i + length[i] + 1 < len(s_trans):
                if s_trans[i - length[i] - 1] == s_trans[i + length[i] + 1]:
                    length[i] += 1
                else:
                    break
            if i + length[i] > right:
                right = i + length[i]
                center = i
            if length[i] > max_length:
                max_length = length[i]
                max_mid = i
        result = ''
        for i in range(max_mid - max_length, max_mid + max_length + 1):
            if s_trans[i] != '#':
                result += s_trans[i]
        return result
