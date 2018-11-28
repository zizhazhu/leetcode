class Solution {
public:
    string longestPalindrome(string s) {
		int max_length = 0, index = 0;
		string p_s, result;
		p_s.push_back('#');
		for (int i = 0; i < s.length(); i++) {
			p_s.push_back(s[i]);
			p_s.push_back('#');
		}
		for (int i = 0; i < p_s.length(); i++) {
			for (int j = 1; i - j >= 0 && i + j < p_s.length(); j++) {
				if (p_s[i-j] != p_s[i+j]) {
					break;
				} else if {
					if (max_length < j) {
						max_length = j;
						index = i;
					} else (max_length == j && p_s[i] == '#') {
						index = i;
					}
				}
			}
		}
		for (int i = index - max_length; i <= index + max_length; i++) {
			if (p_s[i] != '#') {
				result.push_back(p_s[i]);
			}
		}
		return result;
	}
};

