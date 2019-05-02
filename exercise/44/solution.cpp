class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> match(s.length() + 1, vector<bool>(p.length() + 1, false));
        match[0][0] = true;
        for (int i = 0; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                if (i > 0 && match[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '?' || p[j-1] == '*')) {
                    match[i][j] = true;
                }
                if (i > 0 && match[i-1][j] && p[j-1] == '*') {
                    match[i][j] = true;
                }
                if (match[i][j-1] && p[j-1] == '*') {
                    match[i][j] = true;
                }
            }
        }
        return match[s.length()][p.length()];
    }
};
