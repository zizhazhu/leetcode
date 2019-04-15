class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) {
            return 0;
        } else if (haystack.empty()) {
            return -1;
        }
        int m = haystack.length(), n = needle.length();
        int i = 0, j = -1;
        vector<int> next(n + 1);
        next[0] = -1;
        while (i < n) {
            if (j == -1 || needle[i] == needle[j]) {
                i++, j++;
                next[i] = j;
            } else {
                j = next[j];
            }
        }
        i = j = 0;
        while (i < m && j < n) {
            if (j == -1 || haystack[i] == needle[j]) {
                i++, j++;
            } else {
                j = next[j];
            }
        }
        if (j == n) {
            return i - j;
        } else {
            return -1;
        }
    }
};
