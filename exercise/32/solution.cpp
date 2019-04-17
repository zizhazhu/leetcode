class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> valid(s.length());
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ')') {
                if (i > 0 && s[i-1] == '(') {
                    valid[i] = 2;
                } else if (i > 0 && valid[i-1] > 0) {
                    int pair = i - valid[i-1];
                    if (s[pair] == '(') {
                        valid[i] = valid[i-1] + 2;
                    }
                }
                if (i - valid[i] > 0) {
                    valid[i] += valid[i - valid[i]];
                }
            }
            if (max < valid[i]) {
                max = valid[i];
            }
        }
        return max;
    }
};
