class Solution {
public:
    int myAtoi(string str) {
        if (str.length() == 0) {
            return 0;
        }
        int state = 0, pos = 0, sign = 1, num = 0, overflow = 0;
        while (true) {
            if (pos == str.length()) {
                state = 2;
            }
            switch (state) {
                case 0:
                    if (str[pos] == ' ') {
                        ;
                    } else if (str[pos] == '+') {
                        state = 3;
                    } else if (str[pos] == '-') {
                        sign = -1;
                        state = 3;
                    } else if (str[pos] >= '0' && str[pos] <= '9') {
                        num = str[pos] - '0';
                        state = 1;
                    } else {
                        state = 2;
                    }
                    break;
                case 3:
                    if (str[pos] >= '0' && str[pos] <= '9') {
                        num = str[pos] - '0';
                        state= 1;
                    } else {
                        state = 2;
                    }
                    break;
                case 1:
                    if (str[pos] >= '0' && str[pos] <= '9') {
                        int now = str[pos] - '0';
                        if (sign == -1) {
                            if (num == 214748364 && now >= 8 || num > 214748364) {
                                state = 2;
                                overflow = 1;
                            } else {
                                num *= 10;
                                num += now;
                            }
                        } else {
                            if (num == 214748364 && now >= 7 || num > 214748364) {
                                state = 2;
                                overflow = 1;
                            } else {
                                num *= 10;
                                num += now;
                            }
                        }
                    } else {
                        state = 2;
                    }
                    break;
                case 2:
                    if (overflow == 1) {
                        if (sign == 1) {
                            return 2147483647;
                        } else {
                            return -2147483648;
                        }
                    } else {
                        return sign * num;
                    }
            }
            pos++;
        }
    }
};
