class Solution {
public:
    string intToRoman(int num) {
        string roman = "IVXLCDM";
        string result;
        int tnum = num, pos = 0;
        while (tnum) {
            string delta = "";
            int digit = tnum % 10;
            tnum /= 10;
            switch (digit) {
                case 9:
                    delta.push_back(roman[pos]);
                    delta.push_back(roman[pos+2]);
                    break;
                case 8:
                    delta.push_back(roman[pos]);
                case 7:
                    delta.push_back(roman[pos]);
                case 6:
                    delta.push_back(roman[pos]);
                case 5:
                    delta = roman[pos+1] + delta;
                    break;
                case 4:
                    delta.push_back(roman[pos]);
                    delta.push_back(roman[pos+1]);
                    break;
                case 3:
                    delta.push_back(roman[pos]);
                case 2:
                    delta.push_back(roman[pos]);
                case 1:
                    delta.push_back(roman[pos]);
            }
            result = delta + result;
            pos += 2;
        }
        return result;
    }
};
