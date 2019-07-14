class Solution {
public:
    bool isDigit(char c) {
        return c >= '0' && c <= '9';
    }
    bool isNumber(string s) {
        int state = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (state) {
                case 0:
                    if (s[i] == ' ') {
                        state = 0;
                    } else if (s[i] == '+' || s[i] == '-') {
                        state = 7;
                    } else if (isDigit(s[i])) {
                        state = 1;
                    } else if (s[i] == '.') {
                        state = 6;
                    } else {
                        return false;
                    }
                    break;
                case 1:
                    if (isDigit(s[i]))
                        state = 1;
                    else if (s[i] == '.')
                        state = 2;
                    else if (s[i] == 'e')
                        state = 3;
                    else if (s[i] == ' ')
                        state = 5;
                    else
                        return false;
                    break;
                case 2:
                    if (isDigit(s[i]))
                        state = 2;
                    else if (s[i] == 'e')
                        state = 3;
                    else if (s[i] == ' ')
                        state = 5;
                    else
                        return false;
                    break;
                case 3:
                    if (isDigit(s[i]))
                        state = 4;
                    else
                        return false;
                    break;
                case 4:
                    if (isDigit(s[i]))
                        state = 4;
                    else if (s[i] == ' ')
                        state = 5;
                    else
                        return false;
                    break;
                case 5:
                    if (s[i] == ' ')
                        state = 5;
                    else
                        return false;
                    break;
                case 6:
                    // begin with a . or . after sign
                    if (isDigit(s[i]))
                        state = 2;
                    else
                        return false;
                    break;
                case 7:
                    // begin with sign
                    if (isDigit(s[i]))
                        state = 1;
                    else if (s[i] == '.')
                        state = 6;
                    else
                        return false;
            }
        }
        if (state == 0 || state == 3 || state == 4 || state == 6 || state == 7)
            return false;

        return true;
    }
};
