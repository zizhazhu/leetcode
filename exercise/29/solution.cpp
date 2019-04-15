class Solution {
public:
    int divide(int dividend, int divisor) {
        int result = 0;
        if (dividend == 0) {
            return 0;
        } else if (dividend == -2147483648 and divisor == -1) {
            return 2147483647;
        } else if (dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0) {
            while (abs(dividend) >= abs(divisor)) {
                dividend -= divisor;
                result++;
            }
        } else if (dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0) {
            while (abs(dividend) >= abs(divisor)) {
                dividend += divisor;
                result--;
            }
        }
        return result;
    }
};
