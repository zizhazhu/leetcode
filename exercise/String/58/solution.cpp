class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0, now = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ') {
                if (now > 0) {
                    length = now;
                }
                now = 0;
            } else {
                now++;
            }
        }
        if (now > 0) length = now;
        return length;
    }
};
