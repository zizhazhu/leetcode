class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (words.empty()) {
            return result;
        }
        int length = words[0].length();
        int total_length = length * words.size();
        if (total_length > s.length()) {
            return result;
        }
        // count all the words in words
        unordered_map<string, int> words_all;
        for (int j = 0; j < words.size(); j++) {
            words_all[words[j]]++;
        }
        // emumerate the offset
        for (int i = 0; i < length; i++) {
            unordered_map<string, int> words_now;
            int head = i, tail = i;
            while (head + total_length <= s.length() && tail + length <= s.length()) {
                string word = s.substr(tail, length);
                if (words_all.find(word) == words_all.end()) {
                    head = tail = tail + length;
                    words_now.clear();
                    continue;
                }
                words_now[word]++;
                tail += length;
                if (words_now[word] <= words_all[word]) {
                    if ((tail - head) / length == words.size()) {
                        result.push_back(head);
                        words_now[s.substr(head, length)]--;
                        head += length;
                    }
                } else {
                    while (words_now[word] > words_all[word]) {
                        words_now[s.substr(head, length)]--;
                        head += length;
                    }
                }
            }
        }
        return result;
    }
};
