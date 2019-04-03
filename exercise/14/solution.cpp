class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result = "";
        if (strs.size() == 0) {
            return result;
        }
        int pos = 0;
        while (true) {
            char now;
            if (pos < strs[0].length()) {
                now = strs[0][pos];
            } else {
                return result;
            }
            for (int i = 1; i < strs.size(); i++) {
                if (pos < strs[i].length() && now == strs[i][pos]) {
                    continue;
                }
                return result;
            }
            result += now;
            pos++;
        }
        return result;
    }
};
