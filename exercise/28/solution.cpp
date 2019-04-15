class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) {
            return 0;
        } else if (haystack.empty()) {
            return -1;
        }
        int m = haystack.length(), n = needle.length();
        for (int i = 0; i <= m - n ; i++) {
            bool same = true;
            for (int j = 0; j < n; j++) {
                if (haystack[i+j] != needle[j]) {
                    same = false;
                    break;
                }
            }
            if (same) {
                return i;
            }
        }
        return -1;
    }
};
