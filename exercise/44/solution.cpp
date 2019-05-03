class Solution {
public:
    bool isMatch(string s, string p) {
        vector<bool> match(p.length() + 1, false);
        match[0] = true;
        int pre, next_pre;
        for (int i = 0; i <= s.length(); i++) {
            pre = match[0];
            if (i > 0) match[0] = false;
            for (int j = 1; j <= p.length(); j++) {
                next_pre = match[j];
                if (p[j-1] != '*') {
                    match[j] = false;
                }
                if (match[j-1] && p[j-1] == '*') {
                    match[j] = true;
                }
                if (i > 0 && pre && (s[i-1] == p[j-1] || p[j-1] == '?')) {
                    match[j] = true;
                }
                pre = next_pre;
            }
        }
        return match[p.length()];
    }
};
