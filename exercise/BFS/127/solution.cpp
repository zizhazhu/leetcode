class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict, front, back;
        for (const string& word: wordList) {
            dict.insert(word);
        }
        if (dict.find(endWord) == dict.end()) {
            return 0;
        } else {
            dict.erase(endWord);
        }
        front.insert(beginWord);
        back.insert(endWord);

        int level = 2;
        unordered_set<string> *now, *other;
        while (!front.empty() && !back.empty()) {
            if (front.size() <= back.size()) {
                now = &front;
                other = &back;
            } else {
                now = &back;
                other = &front;
            }
            unordered_set<string> next;
            for (const string& word: *now) {
                for (int i = 0; i < word.length(); i++) {
                    string new_word = word;
                    for (int c = 'a'; c <= 'z'; c++) {
                        new_word[i] = c;
                        if (other->find(new_word) != other->end())
                            return level;
                        if (dict.find(new_word) != dict.end()) {
                            dict.erase(new_word);
                            next.insert(new_word);
                        }
                    }
                }
            }
            *now = next;
            level++;
        }
        return 0;
    }
};
