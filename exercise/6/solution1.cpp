class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        string result;
        int gap = 2 * numRows - 2;
        for (int i = 0; i < s.length(); i += gap) {
            result.push_back(s[i]);
        }
        for (int i = 1; i < numRows - 1; i++) {
            for (int j = 0; j * gap + i < s.length(); j++) {
                result.push_back(s[j * gap + i]);
                if (j * gap + 2 * numRows - 2 - i < s.length()) {
                    result.push_back(s[j * gap + 2 * numRows - 2 - i]);
                }
            }
        }
        for (int i = numRows - 1; i < s.length(); i += gap) {
            result.push_back(s[i]);
        }
        return result;
    }
};
