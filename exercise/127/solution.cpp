class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string, int> reached;
        for (int i = 0; i < wordList.size(); i++) {
            reached[wordList[i]] = 0;
        }

        queue<pair<string, int>> fifo;
        fifo.push(make_pair(beginWord, 1));
        reached[beginWord] = 1;

        while (!fifo.empty()) {
            pair<string, int> now = fifo.front();
            fifo.pop();
            int length = now.second;
            for (int i = 0; i < now.first.length(); i++) {
                string word = now.first;
                for (char c = 'a'; c <= 'z'; c++) {
                    word[i] = c;
                    if (word == endWord) {
                        return length + 1;
                    }
                    if (reached.find(word) != reached.end() && reached[word] == 0) {
                        reached[word] = 1;
                        fifo.push(make_pair(word, length + 1));
                    }
                }
            }
        }
        return 0;
    }
};
