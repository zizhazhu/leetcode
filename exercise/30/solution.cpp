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
        unordered_map<string, int> words_all;
        for (int j = 0; j < words.size(); j++) {
            words_all[words[j]]++;
        }
        for (int i = 0; i + total_length <= s.length(); i++) {
            unordered_map<string, int> words_part;
            bool all = true;
            for (int j = 0; i + j * length < i + total_length; j++) {
                string part = s.substr(i + j * length, length);
                if (words_part[part] < words_all[part]) {
                    words_part[part]++;
                } else {
                    all = false;
                    break;
                }
            }
            if (all) {
                result.push_back(i);
            }
        }
        return result;
    }
};
