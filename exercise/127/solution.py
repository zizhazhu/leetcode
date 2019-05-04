class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.remove(endWord)
        wordSet = set(wordList)
        now_queue = [beginWord]
        back_queue = [endWord]
        layer = 2
        while len(now_queue) > 0:
            next_queue = []
            for word in now_queue:
                for i in range(len(word)):
                    new_word_list = list(word)
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word_list[i] = c
                        new_word = ''.join(new_word_list)
                        if new_word in back_queue:
                            return layer
                        if new_word in wordSet:
                            next_queue.append(new_word)
                            wordSet.remove(new_word)
            if len(next_queue) > len(back_queue):
                now_queue = back_queue
            else:
                now_queue = next_queue
            layer += 1
        return 0
