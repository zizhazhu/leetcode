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
        for (int i = 0; i + total_length <= s.length(); i++) {
            map<string, int> words_hash;
            for (int j = 0; j < words.size(); j++) {
                words_hash[words[j]]++;
            }
            bool all = true;
            for (int j = 0; i + j * length < i + total_length; j++) {
                string part = s.substr(i + j * length, length);
                if (words_hash.find(part) != words_hash.end() && words_hash[part] != 0) {
                    words_hash[part]--;
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
