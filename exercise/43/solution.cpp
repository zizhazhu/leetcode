class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int> num_array_1, num_array_2;
        for (int i = num1.length() - 1; i >= 0; i--)
            num_array_1.push_back(num1[i] - '0');
        for (int i = num2.length() - 1; i >= 0; i--)
            num_array_2.push_back(num2[i] - '0');
        vector<int> result(num1.length() + num2.length() - 1);
        for (int i = 0; i < num_array_1.size(); i++) {
            for (int j = 0; j < num_array_2.size(); j++) {
                result[i+j] += num_array_1[i] * num_array_2[j];
            }
        }
        for (int i = 0; i < result.size() - 1; i++) {
            result[i+1] += result[i] / 10;
            result[i] %= 10;
        }
        while (result.size() > 1 && result[result.size() - 1] == 0) {
            result.pop_back();
        }
        string result_str;
        for (int i = result.size() - 1; i >= 0; i--) {
            result_str += to_string(result[i]);
        }
        return result_str;
    }
};
