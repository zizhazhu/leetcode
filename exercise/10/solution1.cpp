class Solution {
public:
    bool isMatchN(string s, string p, int m, int n) {
        if (m == s.length()) {
            return n == p.length();
        }
        bool match = (s[m] == p[n] || p[n] == '.');
        if (n + 1 < p.length() && p[n+1] == '*') {
            return isMatchN(s, p, m, n + 2) || match && isMatchN(s, p, m + 2, n);
        } else {
            return match && isMatchN(s, p, m + 1, n + 1);
        }
    }

    bool isMatch(string s, string p) {
        return isMatchN(s, p, 0, 0);
    }
};
