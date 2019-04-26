class Solution {
public:
    string countAndSay(int n) {
        string now = "1";
        for (int i = 1; i < n; i++) {
            string new_now = "";
            char c = '.';
            int count = 0;
            for (int j = 0; j < now.length(); j++) {
                if (now[j] == c) {
                    count++;
                } else {
                    if (count > 0)
                        new_now += to_string(count) + c;
                    c = now[j];
                    count = 1;
                }
            }
            if (count > 0)
                new_now += to_string(count) + c;
            now = new_now;
        }
        return now;
    }
};
