class Solution {
public:
    string longestPalindrome(string s) {
        vector<vector<int>> f(s.length(), vector<int>(s.length(), 0));
		int max_length = 0, left = 0;
		for (int i = 0; i < s.length(); i++) {
			f[i][i] = 1;
			if (max_length < 1) {
				max_length = 1;
				left = i;
			}
		}
		for (int i = 0; i < s.length() - 1; i++) {
			if (s[i] == s[i+1]) {
				f[i][i+1] = 2;
				if (max_length < 2) {
					max_length = 2;
					left = i;
				}
			}
		}
		for (int l = 2; l < s.length(); l++) {
			for (int i = 0; i + l < s.length(); i++) {
				if (s[i] == s[i + l]) {
					if (f[i+1][i+l-1] != 0) {
						f[i][i+l] = f[i+1][i+l-1] + 2;
						if (max_length < f[i][i+l]) {
							max_length = f[i][i+l];
							left = i;
						}
					}
				}
			}
		}
		return s.substr(left, max_length);
    }
};

