class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        if (n == 0) {
            result.push_back("");
        } else {
            for (int i = 0; i < n; i++) {
                vector<string> left = generateParenthesis(i);
                vector<string> right = generateParenthesis(n - i - 1);
                for (int j = 0; j < left.size(); j++) {
                    for (int k = 0; k < right.size(); k++) {
                        result.push_back("(" + left[j] + ")" + right[k]);
                    }
                }
            }
        }
        return result;
    }
};

