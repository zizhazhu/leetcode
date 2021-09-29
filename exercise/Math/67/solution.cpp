class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1, j = b.length() - 1;
        int carry = 0;
        deque<char> result_queue;
        while (i >= 0 && j >= 0) {
            int num_a = a[i] - '0', num_b = b[j] - '0';
            int temp = num_a + num_b + carry;
            result_queue.push_front('0' + (temp & 1));
            carry = temp >> 1;
            i--, j--;
        }
        string *c = &a;
        if (j >= 0) {
            i = j;
            c = &b;
        }
        while (i >= 0) {
            int num_c = (*c)[i] - '0';
            int temp = num_c + carry;
            result_queue.push_front('0' + (temp & 1));
            carry = temp >> 1;
            i--;
        }
        if (carry) {
            result_queue.push_front('1');
        }
        string result;
        for (auto &it: result_queue) {
            result += it;
        }
        return result;
    }
};
