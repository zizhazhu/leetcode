class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        if (strs.empty()) return result;
        unordered_map<char, int> alphabet;
        for (char c = 'a'; c <= 'z'; c++) {
            alphabet[c] = 0;
        }
        unordered_map<string, vector<string>> word_map;
        for (int i = 0; i < strs.size(); i++) {
            unordered_map<char, int> temp_alphabet(alphabet);
            for (int j = 0; j < strs[i].length(); j++)
                temp_alphabet[strs[i][j]]++;
            string uniform;
            for (char c = 'a'; c <= 'z'; c++) {
                uniform += c;
                uniform += temp_alphabet[c];
            }
            if (word_map.find(uniform) == word_map.end())
                word_map[uniform] = vector<string>();
            word_map[uniform].push_back(strs[i]);
        }
        for (unordered_map<string, vector<string>>::iterator it=word_map.begin(); it != word_map.end(); it++) {
            result.push_back(it->second);
        }
        return result;
    }
};
