class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 0) {
            return true;
        }
        stack<char> bracket;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                bracket.push(s[i]);
            } else if (!bracket.empty()) {
                if (s[i] == ')') {
                    if (bracket.top() == '(') {
                        bracket.pop();
                    } else {
                        return false;
                    }
                } else if (s[i] == ']') {
                    if (bracket.top() == '[') {
                        bracket.pop();
                    } else {
                        return false;
                    }
                } else if (s[i] == '}') {
                    if (bracket.top() == '{') {
                        bracket.pop();
                    } else {
                        return false;
                    }
                }
            } else {
                return false;
            }
        }
        return true;
    }
};
