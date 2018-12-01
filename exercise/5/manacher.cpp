class Solution {
public:
    string longestPalindrome(string s) {
		int max_length = 0, pos = 0;
        string p_s;
		p_s.push_back('#');
		for (int i = 0; i < s.length(); i++) {
			p_s.push_back(s[i]);
			p_s.push_back('#');
		}
		vector<int> longest(p_s.length());
		int right = 0, center = 0;
		for (int i = 1; i < p_s.length(); i++) {
			if (i >= right) {
				center = i;
				for (int l = 0; i - l >= 0 && i + l < p_s.length(); l++) {
					if (p_s[i-l] == p_s[i+l]) {
						right = i + l;
						longest[i] = l;
					} else {
                        break;
                    }
				}
			} else {
				if (longest[2 * center - i] < right - i) {
					longest[i] = longest[2 * center - i];
				} else if (longest[2 * center - i] == right - i) {
					longest[i] = right - i;
					center = i;
					for (int l = longest[i] + 1; i - l >= 0 && i + l < p_s.length(); l++) {
						if (p_s[i-l] == p_s[i+l]) {
							right = i + l;
							longest[i] = l;
						} else {
                            break;
                        }
					}
				} else {
					longest[i] = right - i;
				}
			}
			if (max_length < longest[i]) {
				max_length = longest[i];
				pos = i;
			}
		}
		string result;
		for (int i = pos - max_length; i <= pos + max_length; i++) {
			if (p_s[i] != '#') {
				result.push_back(p_s[i]);
			}
		}
		return result;
    }
};

