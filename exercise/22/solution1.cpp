class Solution {
public:
    void generate(vector<string> &result, string now, int left, int right, int n) {
        if (right == n) {
            result.push_back(now);
            return;
        }
        if (right < left) {
            generate(result, now + ")", left, right + 1, n);
        }
        if (left < n) {
            generate(result, now + "(", left + 1, right, n);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generate(result, "", 0, 0, n);
        return result;
    }
};
