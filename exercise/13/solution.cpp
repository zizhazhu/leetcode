class Solution {
public:
    int romanToInt(string s) {
        vector<int> nums;
        for (int i = 0; i < s.length(); i++) {
            switch(s[i]) {
                case 'I':
                    nums.push_back(1);
                    break;
                case 'V':
                    nums.push_back(5);
                    break;
                case 'X':
                    nums.push_back(10);
                    break;
                case 'L':
                    nums.push_back(50);
                    break;
                case 'C':
                    nums.push_back(100);
                    break;
                case 'D':
                    nums.push_back(500);
                    break;
                case 'M':
                    nums.push_back(1000);
            }
        }
        int pos = 0, result = 0;
        while (pos < nums.size()) {
            if (pos < nums.size() - 1 && nums[pos] < nums[pos+1]) {
                result += nums[pos+1] - nums[pos];
                pos += 2;
            } else {
                result += nums[pos];
                pos++;
            }
        }
        return result;
    }
};
