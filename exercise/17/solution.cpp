class Solution {
public:
    vector<string> letterCombinations(string digits) {
		vector<string> keyboard = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		vector<string> result[2];
        if (digits.length() == 0) {
			return result[0];
		}
		int now = 0;
		result[1].push_back("");
		for (int i = 0; i < digits.length(); i++) {
			int digit = digits[i] - '0';
			for (int j = 0; j < result[1-now].size(); j++) {
				for (int k = 0; k < keyboard[digit].length(); k++) {
					result[now].push_back(result[1-now][j] + keyboard[digit][k]);
				}
			}
			now = 1 - now;
			result[now].clear();
		}
		return result[1 - now];
    }
};
