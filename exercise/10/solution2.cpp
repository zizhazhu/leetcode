class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> f(s.length() + 1, vector<bool>(p.length() + 1, false));
        f[s.length()][p.length()] = true;
        for (int i = s.length(); i >= 0; i--) {
            for (int j = p.length() - 1; j >= 0; j--) {
                bool match = i < s.length() && (s[i] == p[j] || p[j] == '.');
                if (j + 1 < p.length() && p[j+1] == '*') {
                    f[i][j] = f[i][j+2] || match && f[i+1][j];
                } else {
                    f[i][j] = match && f[i+1][j+1];
                }
            }
        }
        return f[0][0];
    }
};

