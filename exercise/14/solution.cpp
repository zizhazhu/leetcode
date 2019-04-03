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
                break;
            }
            bool flag = false;
            for (int i = 1; i < strs.size(); i++) {
                if (pos < strs[i].length() && now == strs[i][pos]) {
                    continue;
                }
                flag = true;
                break;
            }
            if (flag) {
                break;
            } else {
                result += now;
            }
        }
        return result;
    }
};
