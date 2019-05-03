class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, i_star = -1, j_star = -1;
        while (i < s.length()) {
            if (s[i] == p[j] || p[j] == '?') {
                i++, j++;
            } else if (p[j] == '*') {
                i_star = i;
                j_star = j;
                j++;
            } else if (i_star >= 0) {
                i_star++;
                i = i_star;
                j = j_star + 1;
            } else {
                return false;
            }
        }
        while (p[j] == '*') j++;
        if (j == p.length()) return true;
        else return false;
    }
};

