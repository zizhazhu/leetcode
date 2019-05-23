class Solution {
public:
    string getPermutation(int n, int k) {
        string result;
        vector<bool> used(n+1);
        int base = 1;
        for (i = 2; i <= n; i++)
            base *= i;
        int res = k - 1;
        while (result.length() < n) {
            base /= n - result.length();
            int no = res / base;
            int count = no;
            for (int i = 1; i <= n; i++) {
                if (!used[i]) {
                    if (count == 0) {
                        result += '0' + i;
                        used[i] = true;
                        break;
                    } else {
                        count--;
                    }
                }
            }
            res = res % base;
        }
        return result;
    }
};
