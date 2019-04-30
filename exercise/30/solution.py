class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        n = len(words)
        if n == 0:
            return result
        length = len(words[0])
        all_counts = {}
        for i in range(len(words)):
            if words[i] in all_counts:
                all_counts[words[i]] += 1
            else:
                all_counts[words[i]] = 1
        for i in range(length):
            counts = {}
            head = 0
            for j in range(i, len(s)-length+1, length):
                now_word = s[j:j+length]
                if now_word not in all_counts:
                    head = j + length
                    counts.clear()
                else:
                    if now_word not in counts:
                        counts[now_word] = 1
                    else:
                        counts[now_word] += 1
                    while head < j and counts[now_word] > all_counts[now_word]:
                        all_counts[s[head:head+length]] -= 1
                        head += length
                    if (j - head) // length == n:
                        result.append(head)
        return result

