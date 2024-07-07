class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = ''
        for i in range(len(s)):
            result += s[(i + k) % len(s)]
        return result
