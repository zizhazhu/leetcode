class Solution {
public:
    bool isMatch(string s, string p) {
        if (s.empty() && p.empty()) {
            return true;
        } else if (p.empty()) {
            return false;
        }
        int pos = 0, state = 0, step = 0;
        char now;
        while (pos <= s.length()) {
            switch (state) {
                case 0:
                    if (step >= p.length()) {
                        return false;
                    }
                    now = p[step];
                    if (step + 1 == p.length() || p[step+1] != '*') {
                        state = 1;
                        step++;
                    } else {
                        state = 2;
                        step += 2;
                    }
                    break;
                case 1:
                    if (pos < s.length() && (now == s[pos] || now == '.')) {
                        pos++;
                        state = 0;
                    } else {
                        return false;
                    }
                    break;
                case 2:
                    if (pos < s.length() && (now == s[pos] || now == '.')) {
                        pos++;
                    } else {
                        state = 0;
                    }
            }
        }
        return true;
    }
};
