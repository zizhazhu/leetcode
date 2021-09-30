class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> result(digits.size());
        int carry = 1;
        for (int i = digits.size() - 1; i >= 0; i--) {
            int temp = digits[i] + carry;
            result[i] = temp % 10;
            carry = temp / 10;
        }
        if (carry == 1) {
            result.insert(result.begin(), carry);
        }
        return result;
    }
};
