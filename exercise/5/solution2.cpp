class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() == 0) {
            return "";
        }
        vector<vector<int>> f(s.length(), vector<int>(s.length(), 0));
		int max_length = 0, left = 0;
		for (int i = 0; i < s.length(); i++) {
			for (int j = i; j >= 0; j--) {
				if (s[j] == s[i] && (i - j < 2 || f[j+1][i-1] == 1)) {
					f[j][i] = 1;
					if (max_length < i - j) {
						max_length = i - j;
						left = j;
					}
				}
			}
		}
		return s.substr(left, max_length);
    }
};

