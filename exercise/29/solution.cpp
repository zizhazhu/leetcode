class Solution {
public:
    int divide(int dividend, int divisor) {
        int result = 0;
        if (dividend == 0) {
            return 0;
        } else if (dividend == -2147483648 and divisor == -1) {
            return 2147483647;
        }
        if (divisor == -2147483648) {
            if (dividend == -2147483648) {
                return 1;
            } else {
                return 0;
            }
        }
        if (dividend == -2147483648) {
            if (divisor < 0) {
                dividend -= divisor;
                result++;
            } else {
                dividend += divisor;
                result--;
            }
        }
        int sign;
        if (dividend < 0 && divisor < 0 || dividend > 0 && divisor > 0) {
            sign = 1;
        } else {
            sign = -1;
        }
        dividend = abs(dividend);
        divisor = abs(divisor);
        if (dividend < divisor) {
            return result;
        }
        int factor = 1, mul_divisor = divisor;
        while ((mul_divisor < (1 << 30)) && (mul_divisor << 1) <= dividend) {
            mul_divisor <<= 1;
            factor <<= 1;
        }
        while (dividend >= divisor) {
            if (dividend >= mul_divisor) {
                dividend -= mul_divisor;
                result += sign * factor;
            }
            mul_divisor >>= 1;
            factor >>= 1;
        }
        return result;
    }
};
