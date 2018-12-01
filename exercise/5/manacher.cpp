static const auto speedup =[](){std::ios::sync_with_stdio(false); std::cin.tie(NULL); return 0;}();
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
                longest[i] = 0;
            } else {
                longest[i] = min(longest[2 * center - i], right - i);
            }
            for (;i - longest[i] - 1 >= 0 && i + longest[i] + 1 < p_s.length() && p_s[i-longest[i]-1] == p_s[i+longest[i]+1]; longest[i]++);
            if (right < i + longest[i]) {
                right = i + longest[i];
                center = i;
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

